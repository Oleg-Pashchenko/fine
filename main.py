import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv(".env")
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


async def start_bot():
    bot = Bot(token=os.environ.get("BOT_TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    from handlers import dp
    asyncio.run(start_bot())

