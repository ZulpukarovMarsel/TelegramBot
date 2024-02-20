import asyncio
from main import main
import logging

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователом")

    except Exception as e:
        print(f"Возникла ошибка: {e}")

