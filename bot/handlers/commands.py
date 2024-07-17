from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from utils.states import ProcessImageStates
from keyboards.history import kb_first_history
from keyboards.books import kb_download_book
from queries.users import add_new_user, get_user
from queries.books import get_all_book

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_new_user(message.from_user.id)
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
    await message.answer(msg, reply_markup=kb_first_history())


@router.message(Command("new"))
async def cmn_add_new_history(message: Message, state: FSMContext):
    await message.answer(
        "➤ Сперва загрузите до 20 детских фотографий в хронологическом порядке"
    )
    await message.answer(
        "➤ Затем опишите события, которые на них происходят. Пример: Семейная прогулка по парку возле дома с пикником с бабушкой и детьми Полиной 2 года и Максимом 7 лет."
    )
    await state.update_data(photo_file_id=[])
    await state.set_state(ProcessImageStates.addImage)


@router.message(Command("books"))
async def cmn_get_all_book(message: Message):
    books = get_all_book(message.from_user.id)
    await message.answer(f"Доступные книги:\n{books}", reply_markup=kb_download_book())
