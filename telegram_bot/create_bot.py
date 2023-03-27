from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import requests
from googletrans import Translator
from collections import deque

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

# Создание очереди дел
queue_of_ex = deque()
token_job = os.getenv('JOB_TOKEN')
translator = Translator()


async def Create_queue_ex():
    r = requests.get(f"https://www.boredapi.com/api/activity")
    data = r.json()
    cur_ex = str(data["activity"])
    # pprint(data)
    api_url = f'https://api.api-ninjas.com/v1/randomimage?category=abstract&width=3840&height=2160'
    response = requests.get(api_url, headers={'X-Api-Key': token_job, 'Accept': 'image/jpg'}, stream=True)
    translation = translator.translate(cur_ex, src='en', dest='ru')
    queue_of_ex.appendleft([response, translation])