from aiogram import types
from aiogram.filters import CommandStart

from src.database.database import dp

from src.utils.shortcuts import typing


@dp.message(CommandStart())
async def command_start(message: types.Message):
    await typing(message)
