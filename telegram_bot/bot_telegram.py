from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string



bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
	print("Бот включён")


#Start
@dp.message_handler(commands = "start")
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Здравсвуйте, чем я могу быть полезен?\nВот список моих команд")
	except:
		 await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


#Help
@dp.message_handler(commands = "help")
async def command_help(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Вот что я умею")
	except:
		 await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")














@dp.message_handler()
async def echo_send(message: types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply('Маты запрещены')
		await message.delete()
	else:
		await bot.send_message(message.from_user.id, message.text)
	'''
	await message.answer(message.text)
	await message.reply(message.text)
	await bot.send_message(message.from_user.id,message)
	'''
executor.start_polling(dp, skip_updates=True, on_startup = on_startup)
