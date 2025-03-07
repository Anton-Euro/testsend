from typing import Annotated

from fastapi import APIRouter, Body

from schemas import Contact
from settings import settings

router = APIRouter()


@router.post("/save")
async def send_message(message: Annotated[Contact, Body()]):
    for user_id in settings.user_ids:
        await settings.tg_bot.send_message(chat_id=user_id, text=f"""
*Name:* {message.name}
*Email:* {message.email}
*Service:* {message.service}
*Phone:* {message.phone}
*Consent:* {message.consent}
""", parse_mode="markdown")
    return "OK"
    