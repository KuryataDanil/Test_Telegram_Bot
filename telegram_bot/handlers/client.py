from aiogram import types, Dispatcher
from create_bot import dp, bot, Create_queue_ex, queue_of_ex
from datetime import datetime
import os
import requests
from googletrans import Translator

from collections import deque

from pprint import pprint

# Data_Base
from data_base import sqlite_db

# Keyboards
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


enter_message = "Вот список моих команд:\n" \
				"*/дата* - показывает текущую дату\n" \
				"*/время* - показывает текущее время\n" \
				"*/погода* - показывает погоду в Ростове-на-Дону\n" \
				"*/Интересные_места_Ростова* - показывает места Ростова, в которых можно с удовольствием провести время\n" \
				"*/Полезный_совет* - даёт совет, который поможет вам в жизни\n" \
				"*/Не_знаю_чем_заняться* - если вам скучно и нечего делать, бот найдёт вам интересное занятие\n" \
				"*/Да_или_нет* - если у вас не получается принять решение, бот поможет вам это сделать"


# Start
# @dp.message_handler(commands = "start")
async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, "Здравствуйте, чем я могу быть полезен?\n" + enter_message, reply_markup=kb_client, parse_mode="Markdown")
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


# Help
# @dp.message_handler(commands = "help")
async def command_help(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, enter_message, reply_markup=kb_client, parse_mode="Markdown")
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


# Дата
async def command_dataNow(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, datetime.now().date())#, reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Время
async def command_timeNow(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, ':'.join(str(datetime.now().time()).split(':'))[:5])#, reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Погода
token_weather = os.getenv('WEATHER_TOKEN')


async def command_weather(message: types.Message):
	try:
		# Запрос
		city = "rostov-on-don"
		r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric&lang=ru")
		data = r.json()
		weather_main_description = data["weather"][0]["main"]
		# weather_description = data["weather"][0]["description"]

		# Словарь погода -> эмоджи
		code_to_smile = {
			"Clear": "Ясно \U00002600",
			"Clouds": "Облачно \U00002601",
			"Rain": "Дождь \U00002614",
			"Drizzle": "Дождь \U00002614",
			"Thunderstorm": "Гроза \U000026A1",
			"Snow": "Снег \U0001F328",
			"Mist": "Туман \U0001F32B",
		}

		if weather_main_description in code_to_smile:
			weather_smile = code_to_smile[weather_main_description]
		else:
			weather_smile = "У вас какая-то необычная погода \U0001F632, лучше выгляните в окно"

		cur_weather = data["main"]["temp"]
		humidity = data["main"]["humidity"]
		pressure = data["main"]["pressure"]
		wind = data["wind"]["speed"]

		if int(cur_weather) < 5:
			cur_weather_smile = "\U0001F976"
		elif int(cur_weather) < 15:
			cur_weather_smile = "\U0001F642"
		elif int(cur_weather) < 25:
			cur_weather_smile = "\U0001F600"
		else:
			cur_weather_smile = "\U0001F975"

		sunrise_times = str(datetime.fromtimestamp(data["sys"]["sunrise"]))[11:16]
		# print(sunrise_times, type(sunrise_times))
		sunset_times = str(datetime.fromtimestamp(data["sys"]["sunset"]))[11:16]
		await bot.send_message(message.from_user.id, f"{weather_smile}\n"
													 f"Температура {cur_weather}° {cur_weather_smile}\n"
													 f"Влажность {humidity}%\nДавление {pressure} мм.рт.ст\n"
													 f"Ветер {wind} м/с\n"
													 f"Восход солнца {sunrise_times}\n"
													 f"Заход солнца {sunset_times}")
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Подгрузка интересных мест из базы данных
async def command_interestingPlaces(message: types.Message):
	await sqlite_db.sql_read(message)


# Случайное занятие
async def command_ex(message: types.Message):
	try:
		'''
		queue_of_ex = deque()
		r = requests.get(f"https://www.boredapi.com/api/activity")
		data = r.json()
		cur_ex = str(data["activity"])
		# pprint(data)
		api_url = f'https://api.api-ninjas.com/v1/randomimage?category=abstract&width=3840&height=2160'
		response = requests.get(api_url, headers={'X-Api-Key': token_job, 'Accept': 'image/jpg'}, stream=True)
		translation = translator.translate(cur_ex, src='en', dest='ru')
		queue_of_ex.append([response, translation])
		'''
		x = queue_of_ex.pop()
		await bot.send_photo(message.from_user.id, x[0].content, x[1].text)
		await Create_queue_ex()
		# pprint(queue_of_ex)
		# await bot.send_message(message.from_user.id, translation.text)
	except:
		await message.reply('Неверная команда')



# Да или нет
translator = Translator()


async def command_yesOrNo(message: types.Message):
	try:
		r = requests.get(f"https://yesno.wtf/api").json()
		await bot.send_video(message.from_user.id, r['image'])
		await bot.send_message(message.from_user.id, translator.translate(r['answer'], src='en', dest='ru').text)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Совет
async def command_advice(message: types.Message):
	try:
		ad = requests.get(f"https://api.adviceslip.com/advice")
		advice_j = ad.json()
		text_to_translate = str(advice_j['slip']['advice'])
		translation = translator.translate(text_to_translate, src='en', dest='ru')
		await message.reply(f"{translation.text}")
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Регистрация хэндлеров
def register_handlers_client(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(command_help, commands=['help'])
	dp.register_message_handler(command_dataNow, commands=['дата'])
	dp.register_message_handler(command_timeNow, commands=['время'])
	dp.register_message_handler(command_weather, commands=['погода'])
	dp.register_message_handler(command_interestingPlaces, commands=['Интересные_места_Ростова'])
	dp.register_message_handler(command_advice, commands=['Полезный_совет'])
	dp.register_message_handler(command_ex, commands=['Не_знаю_чем_заняться'])
	dp.register_message_handler(command_yesOrNo, commands=['Да_или_нет'])
