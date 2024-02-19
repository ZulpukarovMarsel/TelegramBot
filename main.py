from aiogram import types
from config import bot, dp
from aiogram.utils import executer

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executer.start_polling(dp, skip_updates=True)
