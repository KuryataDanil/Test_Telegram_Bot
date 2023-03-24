from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_data = KeyboardButton("/дата")
b_time = KeyboardButton("/время")
b_weather = KeyboardButton("/погода")
b_places = KeyboardButton("/Интересные_места_Ростова")
b_quiz = KeyboardButton("/Квиз")
b_advice = KeyboardButton("/Полезный_совет")
b_ex = KeyboardButton("/Не_знаю_чем_заняться")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b_data, b_time, b_weather).row(b_advice, b_quiz).add(b_places).add(b_ex)