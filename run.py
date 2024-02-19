import asyncio
from main import main

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователом")

    except Exception as e:
        print(f"Возникла ошибка: {e}")

