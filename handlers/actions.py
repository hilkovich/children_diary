from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


router = Router()


@router.callback_query(F.data == "save_story")
async def cmn_save_story(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await callback.message.answer("История сохранена 🎉")
