import asyncio
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

# Декоратор 
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi", reply_markup=reply.start_kb3.as_markup(resize_keyboard=True, input_field_placeholder="Выберите команду"))

@user_private_router.message(Command('test'))
async def test_cmd(message: types.Message):
    await message.answer("test command")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("about command")

@user_private_router.message(Command('faq'))
async def faq_cmd(message: types.Message):
    text = as_marked_section(
        Bold("О нас"),
        "Первый вариант",
        "Второй вариант",
        "Третий вариант",
        "Четвертый вариант",
        marker="👉"
    )
    await message.answer(text.as_html(), reply_markup=reply.start_kb3.as_markup())

@user_private_router.message(F.text, F.text.lower() == "тест")
async def echo(message: types.Message):
    await message.answer("Магический фильтр с текстом", reply_markup=reply.test_kb)

@user_private_router.message(F.photo)
async def echo(message: types.Message):
    await message.answer("Магический фильтр с картинкой")

@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(message.contact.phone_number)

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(str(message.location))
