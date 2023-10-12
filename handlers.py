from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.callback_query(F.data == "student")
async def student_handler(msg: Message):
    await msg.answer(text.facultet, reply_markup=kb.menu1)

#@router.message(F.text.lower() == "student")
#async def student_handler(msg: types.Message):
 #   await msg.reply(text.facultet, reply_markup=kb.menu)

#@router.message(F.text == "Меню")
#@router.message(F.text == "меню")
#@router.message(F.text == "menu")
#@router.message(F.text == "Menu")
#async def menu(msg: Message):
    #await msg.answer(text.menu, reply_markup=kb.menu)

