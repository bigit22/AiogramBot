from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine, AsyncSession

from models.bot import Base
from config.config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST

engine: AsyncEngine = create_async_engine(
    f'postgresql+asyncpg://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}/{POSTGRES_DB}',
)
session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
