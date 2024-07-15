from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.states import ProcessImageStates
from repository.history import add_history
from keyboards.history import kb_create_story, kb_save_story, kb_repeat_story
from repository.prediction import gen_captions, gen_story, gen_message

router = Router()


@router.callback_query(F.data == "new_story")
async def cmn_new_story(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "➤ Сперва загрузите до 20 детских фотографий в хронологическом порядке"
    )
    await callback.message.answer(
        "➤ Затем опишите события, которые на них происходят. Например: Первый день летних каникул Кристины 7 лет."
    )
    await state.update_data(photos=[])
    await state.set_state(ProcessImageStates.addImage)


@router.message(ProcessImageStates.addImage)
async def cmn_process_images(message: Message, state: FSMContext):
    if message.content_type == "photo":
        data = await state.get_data()
        if len(data["photos"]) < 20:
            data["photos"].append(message.photo[-1].file_id)
        else:
            await message.answer("Вы загрузили максимальное количество фотографий")
        await state.set_state(ProcessImageStates.addText)
    else:
        await message.answer("Сейчас необходимо загрузить фотографии")
        await state.set_state(ProcessImageStates.addImage)


@router.message(ProcessImageStates.addText)
async def cmn_process_text(message: Message, state: FSMContext):
    if message.content_type != "photo":
        await state.update_data(descript=message.text)
        await message.answer(
            "Давайте создадим новую историю 🤩", reply_markup=kb_create_story()
        )
    else:
        await message.answer(
            "Сейчас необходимо описать события, которые происходят на фотографиях"
        )
        await state.set_state(ProcessImageStates.addText)


@router.callback_query(F.data == "create_story")
async def cmn_create_story(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Создаю историю...")
    data = await state.get_data()
    captions = gen_captions(data["photos"])
    msg = gen_message(captions, data["descript"])
    history = gen_story(msg).replace("\n\n", "\n")
    await state.update_data(history=history)
    await state.update_data(captions=captions)
    await callback.message.answer(f"{history}", reply_markup=kb_save_story())


@router.callback_query(F.data == "repeat_story")
async def cmn_repeat_story(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    add_history(
        callback.from_user.id,
        data["captions"],
        data["descript"],
        data["history"],
        None,
        0,
    )
    await callback.message.answer(
        "Жаль, что вам не понравилась история 🥺\nСделаем новую?",
        reply_markup=kb_repeat_story(),
    )
