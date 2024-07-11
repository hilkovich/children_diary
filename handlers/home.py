from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from keyboards.users import kb_first_story

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    msg = (
        "Привет 👋\n"
        "Я — ботик, умею создавать и вести книги с индивидуальной историей ребенка.\n\n"
        "Вы сможете:\n"
        "➤  создавать и сохранять книги под разные важные события и даты ребенка;\n"
        "➤  загружать фотографии ребенка, сделанные в разные периоды его жизни;\n"
        "➤  добавлять текст к фотографиям, описывая события, которые на них изображены, или чувства и эмоции, связанные с этими событиями;\n"
        "➤  с помощью искусственного интеллекта этот материал превратить в главу книги;\n"
        "➤  добавлять главу в уже созданные книги;\n"
        "➤  скачивать книги, чтобы распечатать их или поделиться;\n"
        "➤  отправлять книги в социальные сети и мессенджеры."
    )
    await message.answer(msg, reply_markup=kb_first_story())
