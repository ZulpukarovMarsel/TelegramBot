from aiogram import types
from config import bot, dp
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
@dp.message(CommandStart())
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здраствуйте сэр {message.from_user.first_name}")

@dp.message()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

async def main():
    await dp.start_polling(bot, skip_updates=True)


