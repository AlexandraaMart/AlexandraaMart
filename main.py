#import asyncio
import logging
from aiogram import Bot, Dispatcher, types
#from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6258672653:AAFq2N3kTtaAgUr0F-ZbJvQcMsWtOa4QiAA")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message(commands = ["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "main":
    logging.info('hi')
    dp.start_polling(skip_updates=True)
    #asyncio.run(main())