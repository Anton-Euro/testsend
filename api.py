from typing import Annotated

from fastapi import APIRouter, Form
from pydantic import EmailStr

from schemas import Contact
from settings import settings

router = APIRouter()


@router.post("/save")
async def send_message(
    name: Annotated[str, Form()],
    email: Annotated[EmailStr, Form()],
    service: Annotated[str, Form()],
    phonenumber: Annotated[str, Form()]
):
    for user_id in settings.user_ids:
        await settings.tg_bot.send_message(chat_id=user_id, text=f"""
*Name:* {name}
*Email:* {email}
*Service:* {service}
*Phonenumber:* {phonenumber}
""", parse_mode="markdown")
    return "OK"
    