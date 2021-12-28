from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    InProgress = State()
    AdaptiveTest = State()


