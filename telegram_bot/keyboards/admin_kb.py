from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#b_cancel = KeyboardButton("/Отмена")
b_addComponent = KeyboardButton("/Добавить")
b_backToUser = KeyboardButton("/Выйти_из_режима_админа")


kb_admin = ReplyKeyboardMarkup(resize_keyboard = True)

kb_admin.add(b_addComponent).add(b_backToUser)