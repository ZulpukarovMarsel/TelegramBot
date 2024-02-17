from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = ''
storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
