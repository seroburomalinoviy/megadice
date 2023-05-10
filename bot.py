import asyncio
from conf import Token

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random

# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/d3", description="Кинуть кубик Д3"),
        BotCommand(command="/d4", description="Кинуть кубик Д4"),
        BotCommand(command="/d5", description="Кинуть кубик Д5"),
        BotCommand(command="/d6", description="Кинуть кубик Д6"),
    ]
    await bot.set_my_commands(commands)

async def main():

    # Создание бота, диспетчера и хранилища состояний
    bot = Bot(token=Token)

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    async def d3(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 3)
        await message.answer(str(result))

    async def d4(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 4)
        await message.answer(str(result))

    async def d5(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 5)
        await message.answer(str(result))

    async def d6(message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer_dice()


    dp.register_message_handler(d3, commands="d3", state='*')
    dp.register_message_handler(d4, commands="d4", state='*')
    dp.register_message_handler(d5, commands="d5", state='*')
    dp.register_message_handler(d6, commands="d6", state='*')

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    await dp.skip_updates()
    await dp.start_polling()

    # Закрытие хранилища
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())