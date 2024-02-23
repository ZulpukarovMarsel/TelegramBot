import asyncio
import logging
from aiogram import types, Router
from config import bot, dp
from routers import router as main_router

router = Router()
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        dp.include_routers(main_router)
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователом")

    except Exception as e:
        print(f"Возникла ошибка: {e}")

