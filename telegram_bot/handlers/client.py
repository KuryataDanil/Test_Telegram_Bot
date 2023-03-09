from aiogram import types, Dispatcher
from create_bot import dp, bot

#Start
@dp.message_handler(commands = "start")
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Здравсвуйте, чем я могу быть полезен?\nВот список моих команд')
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


#Help
@dp.message_handler(commands = "help")
async def command_help(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Вот что я умею')
	except:
		await message.reply("Напишите боту в ЛС, вот ссылка:\nhttp://t.me/My_Test61_Bot")


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands = ['start'])
	dp.register_message_handler(command_help, commands = ['help'])