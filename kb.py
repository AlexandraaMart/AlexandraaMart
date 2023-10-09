from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu1 = [
    [InlineKeyboardButton(text="Студент", callback_data="student"),
    InlineKeyboardButton(text="Преподаватель", callback_data="teacher")]
]

menu2 = [
    [InlineKeyboardButton(text="ФизМат", callback_data="FizMat"),
    InlineKeyboardButton(text="Филос", callback_data="Filos")],
    [InlineKeyboardButton(text="ИстФак", callback_data="IstFac"),
    InlineKeyboardButton(text="АСИ", callback_data="ASI")]
]

menu3 = [
    [InlineKeyboardButton(text="1", callback_data="1"),
    InlineKeyboardButton(text="2", callback_data="2")],
    [InlineKeyboardButton(text="3", callback_data="3"),
    InlineKeyboardButton(text="4", callback_data="4")],
    [InlineKeyboardButton(text="5", callback_data="5")]
]


menu = [
    [InlineKeyboardButton(text="Расписание", callback_data="timetable"),
    InlineKeyboardButton(text="Экзамены", callback_data="exams")],
    [InlineKeyboardButton(text="Задолжности", callback_data="debts"),
    InlineKeyboardButton(text="Список группы", callback_data="group list")],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])