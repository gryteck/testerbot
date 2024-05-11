import asyncio
from aiogram import types
from src.config import bot


async def typing(message: types.Message):
    await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    await asyncio.sleep(1)
