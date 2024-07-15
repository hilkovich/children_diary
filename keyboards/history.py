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
                text="Повторить запрос", callback_data="repeat_story"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_repeat_story():
    buttons = [
        [
            types.InlineKeyboardButton(text="Повторить", callback_data="create_story"),
            types.InlineKeyboardButton(text="Изменить фото", callback_data="new_story"),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
