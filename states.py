from aiogram.dispatcher.filters.state import State, StatesGroup

class Asosiy(StatesGroup):
    tel_number=State()
    sms_qod=State()
    kutish = State()