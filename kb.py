from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Студент", callback_data="student"),
    InlineKeyboardButton(text="Преподаватель", callback_data="teacher")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="меню", callback_data="menu")]])





menu1 = [
    [InlineKeyboardButton(text="АСИ", callback_data="ASI"),
    InlineKeyboardButton(text="ФизМат", callback_data="FizMat")]
]
menu1 = InlineKeyboardMarkup(inline_keyboard=menu1)

ex_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Студент")]], resize_keyboard=True)
ie_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Студент", callback_data="student")]])