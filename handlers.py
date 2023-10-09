from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()

@router.message(Command("start"))   #функция является обработчиком входящих сообщений
async def menu_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu1)

@router.message(Command("Menu"))
async def menu_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "menu")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
