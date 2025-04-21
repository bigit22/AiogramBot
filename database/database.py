from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine, AsyncSession

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
