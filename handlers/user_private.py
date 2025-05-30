import asyncio
from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()

# Декоратор 
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi")

@user_private_router.message(Command('test'))
async def test_cmd(message: types.Message):
    await message.answer("test command")

@user_private_router.message(Command('about'))
async def test_cmd(message: types.Message):
    await message.answer("about command")

@user_private_router.message(Command('faq'))
async def test_cmd(message: types.Message):
    await message.answer("faq command")

@user_private_router.message()
async def echo(message: types.Message):
    text = message.text

    await message.answer(text)