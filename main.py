from aiogram import types, Dispatcher
from config import bot, dp

async def main():
    await dp.start_polling(bot)

@dp.message()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


