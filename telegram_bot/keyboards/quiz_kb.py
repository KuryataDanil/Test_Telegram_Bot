from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/ответ1")
b2 = KeyboardButton("/ответ2")
b3 = KeyboardButton("/ответ3")
b4 = KeyboardButton("/ответ4")
b_exit = KeyboardButton("/Выход")


kb_quiz = ReplyKeyboardMarkup(resize_keyboard = True)

kb_quiz.row(b1,b2).row(b3,b4).add(b_exit)