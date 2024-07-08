from aiogram import types


def kb_start():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать первую книгу", callback_data="kb_start"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
