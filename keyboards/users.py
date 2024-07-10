from aiogram import types


def kb_first_story():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать первую книгу", callback_data="new_story"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_create_story():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Получить историю", callback_data="create_story"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
