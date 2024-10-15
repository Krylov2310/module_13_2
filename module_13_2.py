from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


"""
Задание выполнялось на:
Phiton 3.9
aiogram 3.25
"""


token = input('Введите ваш токен: ')
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(commands=["help"])
async def greeting(message):
    await message.answer('Домашнее задание по теме "Хендлеры обработки сообщений"'
                         '\nЦель: написать простейшего телеграм-бота, используя асинхронные функции.'
                         '\nЗадача "Бот поддержки (Начало):"'
                         '\nСтудент Крылов Эдуард Васильевич.'
                         '\nДата работы над заданием: 15.10.2024г.')


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, или /help чтобы начать общение.")
    print('Введите команду /start, или /help чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
