from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

TOKEN = config('TOKEN') 
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()
