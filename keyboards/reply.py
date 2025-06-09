from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тест"),KeyboardButton(text="About")],
        [KeyboardButton(text="FAQ")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите команду",
)

del_kb = ReplyKeyboardRemove()


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Тест"),
    KeyboardButton(text="About"),
    KeyboardButton(text="FAQ"),
)

start_kb2.adjust(2, 1)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="new"))


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос 💀", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="Отправить номер ☎️", request_contact=True)
        ],
        [
            KeyboardButton(text="Отправить локацию 🗺️", request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Choose...",
)