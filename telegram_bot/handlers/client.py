from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime

## Data_Base
from data_base import sqlite_db

## Keyboards
from keyboards import kb_client, kb_quiz
from aiogram.types import ReplyKeyboardRemove

# Start
#@dp.message_handler(commands = "start")
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Здравсвуйте, чем я могу быть полезен?\nВот список моих команд', reply_markup=kb_client)
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


# Help
#@dp.message_handler(commands = "help")
async def command_help(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Вот что я умею')
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot", reply_markup=kb_client)

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

# Погода (в разработке)
async def command_weather(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'В разработке')#, reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')

#Подзрузка интересных мест из базы данных 
async def command_interestingPlaces(message : types.Message):
	await sqlite_db.sql_read(message)
	



# Викторина (дописать машину состояний и перенести в отдельный файл)
async def command_startQuiz(message : types.Message):
	try:
		await bot.send_message(message.from_user.id,'Начинаем квиз', reply_markup = ReplyKeyboardRemove())
		await bot.send_message(message.from_user.id,'Вопрос:', reply_markup = kb_quiz)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


async def command_exit(message : types.Message):
	try:
		await bot.send_message(message.from_user.id,'Квиз окончен', reply_markup = ReplyKeyboardRemove())
		await bot.send_message(message.from_user.id, 'Выберете следующее дейсвие',reply_markup=kb_client)
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands = ['start'])
	dp.register_message_handler(command_help, commands = ['help'])
	dp.register_message_handler(command_dataNow, commands = ['дата'])
	dp.register_message_handler(command_timeNow, commands = ['время'])
	dp.register_message_handler(command_weather, commands = ['погода'])
	dp.register_message_handler(command_interestingPlaces, commands = ['Интересные_места_Ростова'])

	dp.register_message_handler(command_exit, commands = ['Выход'])
	dp.register_message_handler(command_startQuiz, commands = ['Квиз'])