from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/дата")
b2 = KeyboardButton("/время")
b3 = KeyboardButton("/погода")

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.row(b1,b2).add(b3)