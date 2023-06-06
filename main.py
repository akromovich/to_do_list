from aiogram import Dispatcher, Bot

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.include_router(todo_router)
if __name__ == '__main__':
    asyncio.run()