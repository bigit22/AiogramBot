from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from google.generativeai.types import GenerateContentResponse

from ai.utils import get_answer, send_separately
from repositories.chat import ChatHistoryRepository

main_router: Router = Router()


@main_router.message(Command('start'))
async def send_welcome(message: Message):
    """sends welcome message"""
    delete_history_button: KeyboardButton = KeyboardButton(text='/delete_history')
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[delete_history_button]]
    )
    await message.answer(
        'Привет! Я бот, который умеет отвечать на все вопросы.',
        reply_markup=keyboard
    )


@main_router.message(Command('delete_history'))
async def delete_history(callback: CallbackQuery):
    """deletes history"""
    repo = ChatHistoryRepository()
    await repo.delete_messages(callback.from_user.id)
    await callback.answer('История очищена!')


@main_router.message()
async def reply(message: Message):
    """replies to the user"""
    repo = ChatHistoryRepository()
    context = await repo.get_messages(message.from_user.id)
    answer: GenerateContentResponse = get_answer(
        prompt=message.text,
        context=context,
    )
    await repo.add_message(
        telegram_id=message.from_user.id,
        message=f'promt: {message.text} response: {answer.text}'
    )
    await send_separately(answer.text, message)
