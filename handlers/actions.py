import re
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.books import kb_new_book
from repository.books import add_book, get_num_book, get_all_book, get_last_book
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
        last_book = get_last_book(message.from_user.id)
        if last_book.book_num < int(message.text):
            await message.answer("Такой книги не существует")
            await state.set_state(ProcessBookStates.numBook)
        else:
            data = await state.get_data()

            add_history(
                message.from_user.id,
                data["photos"],
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
