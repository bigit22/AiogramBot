from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import TELEGRAM_API_TOKEN
from database.database import setup_database
from handlers.main import main_router

bot: Bot = Bot(token=TELEGRAM_API_TOKEN)
storage: MemoryStorage = MemoryStorage()
dp: Dispatcher = Dispatcher(storage=storage)

dp.include_router(main_router)


async def main():
    await setup_database()
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
