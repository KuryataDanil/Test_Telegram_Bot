from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime
import os
import requests
from googletrans import Translator


from pprint import pprint

# Data_Base
from data_base import sqlite_db

# Keyboards
from keyboards import kb_client, kb_quiz
from aiogram.types import ReplyKeyboardRemove

# Start
# @dp.message_handler(commands = "start")
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Здравсвуйте, чем я могу быть полезен?\nВот список моих команд", reply_markup=kb_client)
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


# Help
# @dp.message_handler(commands = "help")
async def command_help(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Вот что я умею', reply_markup=kb_client)
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")

# Дата
async def command_dataNow(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, datetime.now().date())#, reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')

# Время
async def command_timeNow(message : types.Message):
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
		await bot.send_message(message.from_user.id, f"{weather_smile}\nТемпература {cur_weather}° {cur_weather_smile}\nВлажность {humidity}%\nДавление {pressure} мм.рт.ст\nВетер {wind} м/с\nВосход солнца {sunrise_times}\nЗаход солнца {sunset_times}")
		# pprint(data)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


# Подгрузка интересных мест из базы данных
async def command_interestingPlaces(message: types.Message):
	await sqlite_db.sql_read(message)
	

# Случайное занятие
async def command_ex(message: types.Message):
	try:
		r = requests.get(f"https://www.boredapi.com/api/activity")
		data = r.json()
		# pprint(data)
		cur_ex = str(data["activity"])
		translation = translator.translate(cur_ex, src='en', dest='ru')
		await bot.send_message(message.from_user.id, translation.text)

	except:
		await message.reply('Неверная команда')




# Викторина (дописать машину состояний и перенести в отдельный файл)
async def command_startQuiz(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Начинаем квиз', reply_markup=ReplyKeyboardRemove())
		await bot.send_message(message.from_user.id, 'Вопрос:', reply_markup=kb_quiz)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


async def command_exit(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Квиз окончен', reply_markup=ReplyKeyboardRemove())
		await bot.send_message(message.from_user.id, 'Выберете следующее дейсвие', reply_markup=kb_client)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')
##################################################################

# Совет
translator = Translator()
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

	dp.register_message_handler(command_exit, commands=['Выход'])
	dp.register_message_handler(command_startQuiz, commands=['Квиз'])