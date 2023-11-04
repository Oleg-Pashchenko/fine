import random

from aiogram import F, types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from main import dp
from misc import texts
from web.models import session, ShopItems, Users, Orders


class ShopCallback(CallbackData, prefix="my"):
    item_id: int
    command: str


def get_markup(item_id):
    builder = InlineKeyboardBuilder()
    builder.button(text='<', callback_data=ShopCallback(item_id=item_id, command='<'))
    builder.button(text='buy', callback_data=ShopCallback(item_id=item_id, command='Купить'))
    builder.button(text='>', callback_data=ShopCallback(item_id=item_id, command='>'))
    return builder.as_markup()


def get_text(item_id):
    item = session.query(ShopItems).get(item_id)
    return f"{item.name}\nЦена: {item.price}"


def get_image(item_id):
    item = session.query(ShopItems).get(item_id)
    return f'https://olegpash.tech/uploads/{item.image_url}'


@dp.message(F.text == texts.shop_button)
async def shop_command(message: types.Message):
    all_items = session.query(ShopItems).filter(ShopItems.quantity != 0).all()
    await message.answer_photo(photo=get_image(all_items[0].id), caption=get_text(all_items[0].id),
                               reply_markup=get_markup(all_items[0].id))


@dp.callback_query(ShopCallback.filter(F.command == '<'))
async def shop_command_callback(query: CallbackQuery, callback_data: ShopCallback):
    await query.message.delete()
    all_items = session.query(ShopItems).filter(ShopItems.quantity != 0).all()
    prev = all_items[0]
    for item in all_items[1::]:
        if item.id == callback_data.item_id:
            break
        prev = item
    await query.message.answer_photo(photo=get_image(prev.id), caption=get_text(prev.id),
                                     reply_markup=get_markup(prev.id))


@dp.callback_query(ShopCallback.filter(F.command == '>'))
async def shop_command_callback(query: CallbackQuery, callback_data: ShopCallback):
    await query.message.delete()
    all_items = session.query(ShopItems).filter(ShopItems.quantity != 0).all()
    fl = False
    for item in all_items:
        if fl:
            return await query.message.answer_photo(photo=get_image(item.id), caption=get_text(item.id),
                                                    reply_markup=get_markup(item.id))
        if item.id == callback_data.item_id:
            fl = True

    await query.message.answer_photo(photo=get_image(callback_data.item_id), caption=get_text(callback_data.item_id),
                                     reply_markup=get_markup(callback_data.item_id))


@dp.callback_query(ShopCallback.filter(F.command == 'Купить'))
async def shop_command_callback(query: CallbackQuery, callback_data: ShopCallback):
    item = session.query(ShopItems).get(callback_data.item_id)
    if item.quantity == 0:
        return query.answer("Извините, товар закончился!")
    user = session.query(Users).filter(Users.telegram_id == query.message.chat.id).one()
    print(user)
    print(item)
    if user.money >= item.price:
        await query.message.delete()
        order = Orders(
            owner_id=query.message.chat.id,
            order_secret_key=random.randint(10000, 100000),
            buy_price=item.price,
            user_id=user.id,
            item_id=item.id,
            stage='created'
        )
        item.quantity -= 1
        session.add(order)
        session.commit()
        return await query.message.answer("Благодарим за покупку")
    else:
        return await query.answer("Недостаточно средств!")
