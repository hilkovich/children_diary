from aiogram import types, Router
from aiogram.filters.command import Command

from keyboards.users import kb_start

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    msg = """Привет
            Я - ботик, через который можно загрузить детские фотографии
            и получить альбом с фотографиями и историй сгенерированный
            искусственным интеллектом.
            Альбом включает в себя историю в виде текстовой информации в формате
            рассказа разного жанра и сюжета (например: приключения, комикс,
            будущая профессия, сказка), описание моментов, которые происходят
            на фотографиях, а также самих фотографий."""
    await message.answer(msg, reply_markup=kb_start())
