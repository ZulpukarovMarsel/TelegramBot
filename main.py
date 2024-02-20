from aiogram import types
from config import bot, dp
from aiogram.filters import Command
async def main():
    await dp.start_polling(bot, skip_updates=True)

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здраствуйте сэр {message.from_user.first_name}")
    # await message.answer('Здравствуйте сэр!')
    # await message.reply('Здравствуйте сэр!')

@dp.message(Command('quiz'))
async def quiz_1(message: types.Message):
    question = 'Кто придумал Iphone'
    answer = [
        'Mark',
        'Mars',
        'Стив Джобс'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
        )
    
@dp.message()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


