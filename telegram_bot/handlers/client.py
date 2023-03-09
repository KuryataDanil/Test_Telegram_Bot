from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#Start
#@dp.message_handler(commands = "start")
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Здравсвуйте, чем я могу быть полезен?\nВот список моих команд', reply_markup=kb_client)
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


#Help
#@dp.message_handler(commands = "help")
async def command_help(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Вот что я умею')
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot", reply_markup=kb_client)

#Дата
async def command_dataNow(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, datetime.now().date(), reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')

#Время
async def command_timeNow(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, ':'.join(str(datetime.now().time()).split(':'))[:5], reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')

#Погода (в разработке)
async def command_weather(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'В разработке', reply_markup = ReplyKeyboardRemove())
	except:
		await bot.send_message(message.from_user.id, 'Неверная команда')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands = ['start'])
	dp.register_message_handler(command_help, commands = ['help'])
	dp.register_message_handler(command_dataNow, commands = ['дата'])
	dp.register_message_handler(command_timeNow, commands = ['время'])
	dp.register_message_handler(command_weather, commands = ['погода'])