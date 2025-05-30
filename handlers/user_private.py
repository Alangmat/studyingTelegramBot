import asyncio
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

# Декоратор 
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi")

@user_private_router.message(Command('test'))
async def test_cmd(message: types.Message):
    await message.answer("test command")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("about command")

@user_private_router.message(Command('faq'))
async def faq_cmd(message: types.Message):
    await message.answer("faq command")

@user_private_router.message(F.text, F.text.lower() == "тест")
async def echo(message: types.Message):
    await message.answer("Магический фильтр с текстом")

@user_private_router.message(F.photo)
async def echo(message: types.Message):
    await message.answer("Магический фильтр с картинкой")