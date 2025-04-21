from sqlalchemy import select

from database.database import engine, session
from models.bot import ChatHistory


class ChatHistoryRepository:
    """ChatHistoryRepository"""
    def __init__(self):
        self.engine = engine
        self.session = session

    async def add_message(self, telegram_id: int, message: str):
        """adds message to the history"""
        async with self.session() as se:
            async with se.begin():
                new_message = ChatHistory(telegram_id=telegram_id, message=message)
                se.add(new_message)

    async def get_messages(self, telegram_id: int) -> list[str]:
        """gets messages from the history"""
        async with self.session() as se:
            query = select(ChatHistory).where(
                ChatHistory.telegram_id == telegram_id)
            result = await se.execute(query)
            response = []
            for msg in result.scalars().all():
                response.append(msg.message)
            return response

    async def delete_messages(self, telegram_id: int):
        """deletes messages from the history"""
        async with self.session() as se:
            async with se.begin():
                query = select(ChatHistory).where(
                    ChatHistory.telegram_id == telegram_id)
                result = await se.execute(query)
                for msg in result.scalars().all():
                    await se.delete(msg)
                await se.commit()
