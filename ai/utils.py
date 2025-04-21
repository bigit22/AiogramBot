import google.generativeai as genai
from aiogram.types import Message
from google.ai.generativelanguage import GenerateContentResponse

from config.config import GOOGLE_API_KEY, RESPONSE_MAX_LENGTH

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


def get_answer(prompt: str, context: list[str]) -> GenerateContentResponse:
    """gets answer from the model"""
    ready_prompt = (
        f'Контекст диалога: {context if context else "Нет контекста"}\n'
        f'Пожалуйста, ответь на следующий вопрос по-русски: {prompt}'
    )
    return model.generate_content(ready_prompt)


async def send_separately(answer: str, message: Message) -> None:
    """sends messages separately"""
    part_length = RESPONSE_MAX_LENGTH
    start = 0
    while start < len(answer):
        end = start + part_length
        if end >= len(answer):
            await message.answer(answer[start:])
            break
        last_space = answer.rfind(' ', start, end)
        if last_space == -1:
            last_space = end
        await message.answer(answer[start:last_space])
        start = last_space + 1
