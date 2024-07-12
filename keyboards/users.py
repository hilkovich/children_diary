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


def kb_save_story():
    buttons = [
        [
            types.InlineKeyboardButton(text="Сохранить", callback_data="save_story"),
            types.InlineKeyboardButton(
                text="Показать еще", callback_data="create_story"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


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
