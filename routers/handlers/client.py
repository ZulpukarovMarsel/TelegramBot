from aiogram import types , Router
from config import dp, bot
from aiogram.filters import CommandStart, Command
from database.bot_db import Database
router = Router(name=__name__)

@router.message(CommandStart())
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здраствуйте сэр {message.from_user.full_name}")

@router.message(Command('help', prefix="!/"))
async def handle_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Чем могу помочь")

@router.message(Command('save', prefix="!/"))
async def handle_save(message: types.Message):
    content_type = message.content_type
    content_data = await message.content_data()

    user_id = message.from_user.id
    Database().save_to_database(user_id, content_type, content_data)
    await message.reply("Сохранено!")

@router.message(Command("my_save", prefix="!/"))
async def handle_my_save(message: types.Message):
    user_id = message.from_user.id

    saved_data = Database().select_from_database(user_id)

    if not saved_data:
        await message.reply("У вас нету сохраненных данных")
        return

    result_message = "Ваши сохраненные данные \n"
    for content_type, content_list in saved_data:
        result_message += f"{content_type.capitalize()}: ({content_list})\n"

    await message.reply(result_message)
