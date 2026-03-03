import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- ЛОГИ ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# --- ТОКЕН ---
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- СТАРТ ---
@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть ❤️", callback_data="open_video")]
        ]
    )

    logger.info(f"User {message.from_user.id} started the bot")

    await message.answer(
        "Ксюша, у меня для тебя кое-что есть.\n\nНо просто так я не отдам 🙂",
        reply_markup=keyboard
    )

# --- КНОПКА ---
@dp.callback_query(lambda c: c.data == "open_video")
async def send_video(callback: types.CallbackQuery):
    await callback.answer()
    logger.info(f"User {callback.from_user.id} clicked open_video")

    await callback.message.answer("Секунду…")
    await asyncio.sleep(2)

    # ПОКА ЗАГЛУШКА
    await callback.message.answer("Видео скоро будет здесь ❤️")

# --- ПОЛУЧЕНИЕ FILE_ID ---
@dp.message(lambda message: message.video is not None)
async def get_video_id(message: types.Message):
    logger.info(f"VIDEO FILE_ID: {message.video.file_id}")
    await message.answer("Видео получил 👌")

# --- ЗАПУСК ---
async def main():
    logger.info("BOT STARTED")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
