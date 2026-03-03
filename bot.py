import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

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

@dp.callback_query(lambda c: c.data == "open_video")
async def send_video(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Подожди секунду…")
    await asyncio.sleep(2)

    video = FSInputFile("video.mp4")
    await callback.message.answer_video(video, caption="С 8 марта ❤️")

async def main():
    await dp.start_polling(bot)

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    print("VIDEO FILE_ID:", video.file_id)

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
