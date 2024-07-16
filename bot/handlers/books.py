import re
import os
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from bot.keyboards import kb_new_book
from bot.repository import (
    add_book,
    get_num_book,
    get_all_book,
    get_one_book,
    get_name_book,
)
from bot.repository import add_history, get_all_history
from bot.utils import ProcessBookStates

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
            data["captions"],
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
    book_id = get_num_book(callback.from_user.id)
    if book_id is None:
        await callback.message.answer("Созданных книг не существует")
    else:
        books = get_all_book(callback.from_user.id)
        await callback.message.answer(f"Доступные книги:\n{books}")
        await callback.message.answer("Укажите номер книги")
        await state.set_state(ProcessBookStates.numBook)


@router.message(ProcessBookStates.numBook)
async def cmn_num_book(message: Message, state: FSMContext):
    if re.findall(r"\d+", message.text):
        last_book = get_num_book(message.from_user.id)
        if last_book.book_num < int(message.text) or int(message.text) == 0:
            await message.answer("Такой книги не существует")
            await state.set_state(ProcessBookStates.numBook)
        else:
            data = await state.get_data()

            add_history(
                message.from_user.id,
                data["captions"],
                data["descript"],
                data["history"],
                int(message.text),
                1,
            )

            await state.clear()
            await message.answer("История сохранена 🎉")
    else:
        await message.answer("Необходимо указать номер книги")
        await state.set_state(ProcessBookStates.numBook)


@router.callback_query(F.data == "show_book")
async def cmn_show_book(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Необходимо указать номер книги")
    await state.set_state(ProcessBookStates.allBook)


@router.message(ProcessBookStates.allBook)
async def cmn_one_book(message: Message, state: FSMContext):
    if re.findall(r"\d+", message.text):
        last_book = get_num_book(message.from_user.id)
        if last_book.book_num < int(message.text) or int(message.text) == 0:
            await message.answer("Такой книги не существует")
            await state.set_state(ProcessBookStates.allBook)
        else:
            books = get_all_history(message.from_user.id, int(message.text))
            get_one_book(message.from_user.id, int(message.text), books)
            name_book = get_name_book(message.from_user.id, int(message.text)).book_name

            dir_file = f"books/{message.from_user.id}_{int(message.text)}.docx"
            book_file = FSInputFile(path=dir_file, filename=name_book)
            await message.answer_document(document=book_file)
            os.remove(dir_file)
    else:
        await message.answer("Необходимо указать номер книги")
        await state.set_state(ProcessBookStates.allBook)
