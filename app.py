import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from utils.commands import set_commands
from handlers import home

load_dotenv()

bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher()


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


dp.include_router(home.router)


if __name__ == "__main__":
    asyncio.run(start())
