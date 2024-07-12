from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.books import kb_new_book
from repository.books import add_book, get_num_book, get_all_book
from repository.history import add_history
from utils.states import ProcessBookStates

router = Router()


@router.callback_query(F.data == "save_story")
async def cmn_save_story(callback: CallbackQuery):
    await callback.message.answer(
        "Создайте новую книгу или добавьте главу в вашу книгу",
        reply_markup=kb_new_book(),
    )


@router.callback_query(F.data == "create_book")
async def cmn_create_book(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Как назавем книгу?")
    await state.set_state(ProcessBookStates.addBook)


@router.message(ProcessBookStates.addBook)
async def cmn_name_book(message: Message, state: FSMContext):
    if len(message.text) < 30:
        data = await state.get_data()

        add_book(message.from_user.id, message.text)
        book_id = get_num_book(message.from_user.id).book_num
        add_history(
            message.from_user.id,
            data["photos"],
            data["descript"],
            data["history"],
            book_id,
            1,
        )

        await state.clear()
        await message.answer("Вы создали новую книгу и сохранили историю 🎉")
    else:
        await message.answer("Слишком большое название книги")
        await state.set_state(ProcessBookStates.addBook)


@router.callback_query(F.data == "save_book")
async def cmn_save_book(callback: CallbackQuery, state: FSMContext):
    books = get_all_book(callback.from_user.id)
    await callback.message.answer(f"Доступные книги:\n{books}")
    await callback.message.answer("Укажите номер книги")
    await state.set_state(ProcessBookStates.numBook)


# data = await state.get_data()
# await state.clear()
# await callback.message.answer(f"История сохранена 🎉 \n{all_book}")
