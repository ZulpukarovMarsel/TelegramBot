from aiogram import types, Dispatcher
from aiogram.utils import executor
from config import bot, dp
from handlers import client
import logging
# from database.bot_db import sql_create

async def on_startup(dp: Dispatcher):
    return
    # sql_create()

client.register_handler_client(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)