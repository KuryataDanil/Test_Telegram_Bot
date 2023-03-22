from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_data = KeyboardButton("/дата")
b_time = KeyboardButton("/время")
b_weather = KeyboardButton("/погода")
b_places = KeyboardButton("/Интересные_места_Ростова")
b_quiz = KeyboardButton("/Квиз")
b_advice = KeyboardButton("/Полезный_совет")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b_data, b_time, b_weather).row(b_advice).add(b_places).add(b_quiz)