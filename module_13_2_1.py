from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher, types
import asyncio


"""
Задание выполнялось на:
Phiton 3.12
aiogram 3.13.1
"""

user_token = input('Введите ваш токен: ')
bot = Bot(token=user_token)
dp = Dispatcher()


@dp.message(Command("help"))
async def start_message(message: types.Message):
    text = ('Домашнее задание по теме "Хендлеры обработки сообщений"'
            '\nЦель: написать простейшего телеграм-бота, используя асинхронные функции.'
            '\nЗадача "Бот поддержки (Начало):"'
            '\nСтудент Крылов Эдуард Васильевич.'
            '\nДата работы над заданием: 15.10.2024г.')
    await message.answer(text)
    print(text)


@dp.message(Command("start"))
async def start_message(message: types.Message):
    text = "Привет! Я бот помогающий твоему здоровью."
    await message.answer(text)
    print(text)


@dp.message()
async def all_message(message):
    text = "Введите команду /start, или /help чтобы начать общение."
    await message.answer(text)
    print(text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
