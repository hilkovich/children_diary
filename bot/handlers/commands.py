from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from bot.keyboards.history import kb_first_story
from bot.keyboards import kb_show_book
from bot.utils import ProcessImageStates
from bot.queries import get_user, add_user
from bot.queries import get_all_book

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id)
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


@router.message(Command("new"))
async def cmn_new_story(message: Message, state: FSMContext):
    await message.answer(
        "➤ Сперва загрузите до 20 детских фотографий в хронологическом порядке"
    )
    await message.answer(
        "➤ Затем опишите события, которые на них происходят. Например: Первый день летних каникул Кристины 7 лет."
    )
    await state.update_data(photos=[])
    await state.set_state(ProcessImageStates.addImage)


@router.message(Command("books"))
async def cmn_all_books(message: Message):
    books = get_all_book(message.from_user.id)
    await message.answer(f"Доступные книги:\n{books}", reply_markup=kb_show_book())
