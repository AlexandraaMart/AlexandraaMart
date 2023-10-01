from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Расписание", callback_data="generate_text"),
    InlineKeyboardButton(text="Экзамены", callback_data="generate_image")],
    [InlineKeyboardButton(text="Задолжности", callback_data="buy_tokens"),
    InlineKeyboardButton(text="Список группы", callback_data="balance")],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])