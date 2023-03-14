from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot

import os

## Keyboards
from keyboards import kb_admin, kb_client
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



### Кнопка отмены
b_cancel = KeyboardButton("/Отмена")
kb_cancel = ReplyKeyboardMarkup(resize_keyboard = True)
kb_cancel.add(b_cancel)
###

class FSMAdmin(StatesGroup):
	admin_panel = State()
	photo = State()
	name = State()
	desсription = State()

admin_ID = os.getenv('AdminId')

async def cm_start(message : types.Message, state = None):
	if str(message.from_user.id) == admin_ID:
		await FSMAdmin.admin_panel.set()
		await message.reply("Вы вошли в админускую панель", reply_markup = kb_admin)
		await message.delete()
	else:
		await message.reply("Вы не админ данного бота!")
		await message.delete()


#Начало добавления
#########################################################################
async def start_add(message : types.Message, state: FSMContext):
	await FSMAdmin.next()
	await message.reply('Загрузите фото',reply_markup = kb_cancel)


async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply("Теперь введите название")


async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply("Введите краткое описание темы")


async def load_desсription(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['desсription'] = message.text
	await message.reply('Добавление прошло успешно',reply_markup = kb_admin)

	#Временное решение без базы данных (для тестирования)
	async with state.proxy() as data:
		await message.reply(str(data))
	await state.finish()
	await FSMAdmin.admin_panel.set()
#########################################################################


#Отмена добавления 
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await FSMAdmin.admin_panel.set()
	await message.reply('Добавление отменено',reply_markup = kb_admin)

#Выход из панели админа
async def backToUser_handler(message: types.Message, state: FSMContext):
	await message.reply('Вы вышли из панели админа',reply_markup = kb_client)
	await state.finish()


def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(cancel_handler, commands = 'Отмена', state="*")
	dp.register_message_handler(backToUser_handler, commands = ['Выйти_из_режима_админа'], state = FSMAdmin.admin_panel)
	dp.register_message_handler(cm_start, commands=['moderator'], state = None)
	dp.register_message_handler(start_add, commands=['Добавить'], state = FSMAdmin.admin_panel)
	dp.register_message_handler(load_photo, content_types=['photo'], state = FSMAdmin.photo)
	dp.register_message_handler(load_name, state = FSMAdmin.name)
	dp.register_message_handler(load_desсription, state = FSMAdmin.desсription)
	