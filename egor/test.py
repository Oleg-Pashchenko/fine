import http.client
import json
import os
import dotenv
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

dotenv.load_dotenv()

key = os.getenv('IMAGINE_API_KEY')

connection = http.client.HTTPSConnection("demo.imagineapi.dev")

headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

bot = Bot(token=os.getenv('TELEGRAM_API_TOKEN'))
dp = Dispatcher()


async def create_task(prompt: str) -> str:
    data = {"prompt": f"{prompt} --ar 9:21 --chaos 40 --stylize 1000"}
    connection.request("POST", "/items/images/", body=json.dumps(data), headers=headers)
    response = connection.getresponse()
    response_data = json.loads(response.read().decode('utf-8'))
    return response_data['data']['id']


async def get_image_by_task(task_id: str):
    connection.request("GET", f"/items/images/{task_id}", headers=headers)
    response = connection.getresponse()
    data = json.loads(response.read().decode())
    if data['data']['status'] != 'completed':
        await asyncio.sleep(3)
        return await get_image_by_task(task_id=task_id)
    return data['data']['url']


async def generate_image_by_prompt(prompt: str):
    task_id = await create_task(prompt)
    return await get_image_by_task(task_id)


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Image Generation Bot! Send me a prompt, and I'll generate an image for you.")


@dp.message()
async def generate_image(message: types.Message):
    prompt = message.text
    image_url = await generate_image_by_prompt(prompt)

    await message.reply(image_url)


async def start_bot():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
