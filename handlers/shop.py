from aiogram import F, types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from main import dp
from misc import texts


class ShopCallback(CallbackData, prefix="my"):
    item_id: int
    command: str


builder = InlineKeyboardBuilder()
builder.button(text='<', callback_data=ShopCallback(item_id=item_id, command='<'))
builder.button(text='buy', callback_data=ShopCallback(item_id=item_id, command='buy'))
builder.button(text='>', callback_data=ShopCallback(item_id=item_id, command='>'))


@dp.message(F.text == texts.shop_button)
async def shop_command(message: types.Message):
    await message.answer(texts.menu_message, reply_markup=builder.as_markup())


@dp.callback_query(ShopCallback)
async def shop_command_callback(query: CallbackQuery, callback_data: ShopCallback):
    await query.answer('lol')
