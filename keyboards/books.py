from aiogram import types


def kb_new_book():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать книгу", callback_data="create_book"
            ),
            types.InlineKeyboardButton(
                text="Сохранить в книгу", callback_data="save_book"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
