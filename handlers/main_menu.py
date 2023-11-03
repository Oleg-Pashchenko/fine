from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main import dp
from aiogram import types, F
from misc import texts
from web.models import *
# Keyboards
menu_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=texts.profile_button), KeyboardButton(text=texts.activity_button)],
        [KeyboardButton(text=texts.shop_button), KeyboardButton(text=texts.orders_button)]
    ],
    resize_keyboard=True
)


# Handlers
@dp.message(Command(texts.start_command))
async def welcome_command(message: types.Message):
    all_users = session.query(Users).all()
    is_exists = False
    for user in all_users:
        if user.telegram_id == message.chat.id:
            is_exists = True

    if not is_exists:
        user = Users(
            telegram_id=message.chat.id,
            username=message.chat.username,
            first_name=message.chat.first_name,
            last_name=message.chat.last_name,
            money=0
        )
        session.add(user)
        session.commit()
    await message.answer(texts.start_message)
    await menu_command(message)


@dp.message(Command(texts.menu_command))
@dp.message(F.text == texts.back_button)
async def menu_command(message: types.Message):
    await message.answer(texts.menu_message, reply_markup=menu_markup)
