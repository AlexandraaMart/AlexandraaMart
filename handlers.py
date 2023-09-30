from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()

@router.message(Command("start"))   #функция является обработчиком входящих сообщений
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне /id")

@router.message(Command("end"))   #функция является обработчиком входящих сообщений
async def end_handler(msg: Message):
    await msg.answer("Пока! Если понадоблюсь, то я тут")

@router.message(Command("id"))
async def id_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")

@router.message(Command("Menu"))
async def menu_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
