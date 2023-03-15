from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#b_cancel = KeyboardButton("/Отмена")
b_addComponent = KeyboardButton("/Добавить")
b_delComponent = KeyboardButton("/Удалить")
b_backToUser = KeyboardButton("/Выйти_из_режима_админа")


kb_admin = ReplyKeyboardMarkup(resize_keyboard = True)

kb_admin.row(b_addComponent,b_delComponent).add(b_backToUser)