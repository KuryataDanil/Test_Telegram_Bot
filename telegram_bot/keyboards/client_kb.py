from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_data = KeyboardButton("/дата")
b_time = KeyboardButton("/время")
b_weather = KeyboardButton("/погода")
b_places = KeyboardButton("/Интересные_места_Ростова")
b_yesOrNo = KeyboardButton("/Да_или_нет")
b_advice = KeyboardButton("/Полезный_совет")
b_ex = KeyboardButton("/Не_знаю_чем_заняться")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b_data, b_time, b_weather).row(b_advice, b_yesOrNo).add(b_ex).add(b_places)