from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/дата")
b2 = KeyboardButton("/время")
b3 = KeyboardButton("/погода")
b4 = KeyboardButton("/Интересные_места_Ростова")
b5 = KeyboardButton("/Квиз")

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.row(b1,b2).add(b3).add(b4).add(b5)