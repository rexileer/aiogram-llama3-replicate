from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

generation_image_text = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Сгенерировать фото'), KeyboardButton(text='Сгенерировать текст')],
],                               resize_keyboard=True,)

back_button =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главное меню')]
],                               resize_keyboard=True)
