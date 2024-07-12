from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.users import kb_new_book

router = Router()


@router.callback_query(F.data == "save_story")
async def cmn_save_story(callback: CallbackQuery):
    await callback.message.answer(
        "Создайте новую книгу или добавьте главу в ваши книги",
        reply_markup=kb_new_book(),
    )


@router.callback_query(F.data == "")
async def cmn_save_story(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await callback.message.answer("История сохранена 🎉")
