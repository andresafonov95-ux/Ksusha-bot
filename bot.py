import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Стартовое сообщение
@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть ❤️", callback_data="open_video")]
        ]
    )
    await message.answer(
        "Ксюша, у меня для тебя кое-что есть.\n\nНо просто так я не отдам 🙂",
        reply_markup=keyboard
    )

# Отправка видео по кнопке (пока просто заглушка)
@dp.callback_query(lambda c: c.data == "open_video")
async def send_video(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Секунду…")
    await asyncio.sleep(2)

    # ВРЕМЕННО: сюда вставим file_id позже
    await callback.message.answer("Видео скоро будет здесь ❤️")

# Обработчик видео — чтобы получить file_id
@dp.message(lambda message: message.video is not None)
async def get_video_id(message: types.Message):
    print("VIDEO FILE_ID:", message.video.file_id)
    await message.answer("Видео получил 👌")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
