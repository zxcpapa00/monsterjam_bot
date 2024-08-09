from aiogram.fsm.state import StatesGroup, State


class AddSource(StatesGroup):
    add = State()


class StartStopParser(StatesGroup):
    start = State()
