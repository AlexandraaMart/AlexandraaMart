import asyncio
from aiogram import Bot, Dispatcher, types

# Создание экземпляра бота и диспетчера
bot = Bot(token="6258672653:AAFq2N3kTtaAgUr0F-ZbJvQcMsWtOa4QiAA")
dp = Dispatcher()

# Обработчик команды /start
@dp.message(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я асинхронный бот.")

# Обработчик текстовых сообщений
@dp.message(content_types=types.ContentType.TEXT)
async def echo(message: types.Message):
    await message.answer(message.text)

# Функция запуска бота
async def main():
    # Старт бота
    await bot.start_polling()

# Запуск функции main в асинхронном режиме
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
