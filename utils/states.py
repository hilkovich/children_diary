from aiogram.fsm.state import StatesGroup, State


class ProcessImageStates(StatesGroup):
    addImage = State()
    addText = State()
    addBook = State()
