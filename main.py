from aiogram import types
from config import bot, dp
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def main():
    await dp.start_polling(bot, skip_updates=True)

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здраствуйте сэр {message.from_user.first_name}")
    # await message.answer('Здравствуйте сэр!')
    # await message.reply('Здравствуйте сэр!')

@dp.message_handler(Command('quiz'))
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[])
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    markup.add(button_call_1)

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
        correct_option_id=2,
        explanation='Не шаришь',
        open_period=10,
        reply_markup=markup
        )
@dp.callback_query(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.callback_query):
    markup = InlineKeyboardMarkup(inline_keyboard=[])
    button_call_2 = InlineKeyboardButton(callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Кто придумал Python'
    answer = [
        'Mark',
        'Mars',
        'Стив Джобс',
        'Guido Van Rossum'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Не шаришь',
        open_period=10,
        reply_markup=markup
        )
@dp.message()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


