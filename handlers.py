from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import aiofiles
from settings import settings

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, command: CommandObject):
    if command.args != settings.PASSWORD:
        await message.answer(f"incorrent password")
        return
    user_id = str(message.from_user.id)

    async with aiofiles.open(settings.USER_IDS_PATH, mode="a+", encoding="utf-8") as f:
        await f.seek(0) 
        content = await f.read()
        if user_id not in content.splitlines():
            await f.write(user_id + "\n")
    settings.user_ids.append(user_id)

    await message.answer(f"start recive")
