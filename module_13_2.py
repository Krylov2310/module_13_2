from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


"""
Задание выполнялось на:
Phiton 3.9
aiogram 3.25
"""

user_token = input('Введите ваш токен: ')
bot = Bot(token=user_token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["help"])
async def greeting(message):
    text = ('Домашнее задание по теме "Хендлеры обработки сообщений"'
            '\nЦель: написать простейшего телеграм-бота, используя асинхронные функции.'
            '\nЗадача "Бот поддержки (Начало):"'
            '\nСтудент Крылов Эдуард Васильевич.'
            '\nДата работы над заданием: 15.10.2024г.')
    await message.answer(text)
    print(text)


@dp.message_handler(commands=["start"])
async def start_message(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    await message.answer(text)
    print(text)


@dp.message_handler()
async def all_message(message):
    text = "Введите команду /start, или /help чтобы начать общение."
    await message.answer(text)
    print(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
