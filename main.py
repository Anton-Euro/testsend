import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router
from handlers import router as tg_router
from settings import settings
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:3000/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

async def start_bot():
    logging.basicConfig(level=logging.INFO)
    settings.dp.include_router(tg_router)
    await settings.dp.start_polling(settings.tg_bot)


async def start_fastapi():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    bot_task = asyncio.create_task(start_bot())
    api_task = asyncio.create_task(start_fastapi())

    await asyncio.gather(bot_task, api_task)


if __name__ == "__main__":
    asyncio.run(main())