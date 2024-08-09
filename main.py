import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from database.db import db_start
from routers.parser.parser_handler import router as parser_router
from routers.commands.commands_handler import router as command_router
from routers.user.user_handler import router as user_router
from routers.post.post_handler import router as post_router

load_dotenv()

TOKEN = os.getenv("API_KEY")
bot = Bot(token=TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML,
))
dp = Dispatcher(storage=MemoryStorage())

dp.include_routers(parser_router, command_router, user_router, post_router)


async def main():
    await db_start()
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
