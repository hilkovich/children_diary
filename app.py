import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from utils.commands import set_commands
from handlers import command, stories, actions

load_dotenv()

bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher()


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


dp.include_router(command.router)
dp.include_router(stories.router)
dp.include_router(actions.router)


if __name__ == "__main__":
    asyncio.run(start())
