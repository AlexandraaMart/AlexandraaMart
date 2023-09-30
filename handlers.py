from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))   #функция является обработчиком входящих сообщений
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")

@router.message(Command("end"))   #функция является обработчиком входящих сообщений
async def end_handler(msg: Message):
    await msg.answer("Пока! Если понадоблюсь, то я тут")

@router.message() #реагирует на все сообщения, так как у него не задан ни один фильтр
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


