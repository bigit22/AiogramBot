"""models.py"""
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    """Base"""
    pass


class ChatHistory(Base):
    """ChatHistory"""
    __tablename__ = 'chat_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int]
    message: Mapped[str]
