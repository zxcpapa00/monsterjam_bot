from aiogram.fsm.state import State, StatesGroup


class AddText(StatesGroup):
    add = State()


class AddMedia(StatesGroup):
    add_photo = State()


class AddSignature(StatesGroup):
    add = State()


class AddSignatureText(StatesGroup):
    add = State()


class AddSignatureUrl(StatesGroup):
    add = State()
