from aiogram import Router, Command, types

todo_router = Router()


@todo_router.message(Command('start'))
async def start(msg: types.Message):
    await msg.reply('Hello')
