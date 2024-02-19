from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = '6384356816:AAEZclC-3x-Zg4A9y36MCKP9wjpw6bcVv38'
storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
# dp = Dispatcher(bot=bot, storage=storage)
