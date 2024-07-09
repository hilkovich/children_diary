from aiogram.fsm.state import StatesGroup, State


class ProcessImageStates(StatesGroup):
    startImage = State()
    finishImage = State()
