import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

TOKEN = os.getenv("TOKEN")
VIDEO_ID = os.getenv("VIDEO_ID")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

'''@dp.message(lambda message: message.photo)
async def get_photo_id(message: types.Message):
    photo = message.photo[-1]
    print("PHOTO_ID:", photo.file_id)
    await message.answer("Фото получил 👌")'''

@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🐱", callback_data="open_video")]
        ]
    )

    text = """
Ксюша.

Ты иногда говоришь, что не веришь, что я тебя люблю по-настоящему.
Наверное потому, что я не всегда умею говорить об этом правильно

Но для меня это правда.

И я знаю, что ты больше веришь поступкам, чем словам.
Поэтому я сделал для тебя этот маленький сюрприз. Немного провозился с ним😄

Просто чтобы ты улыбнулась и знала, ты для меня очень важна.

Нажми кнопку 🐱 и посмотри
"""

    await message.answer(text, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "open_video")
async def send_video(callback: types.CallbackQuery):
    await callback.answer()

    user = callback.from_user

    await bot.send_message(
        ADMIN_ID,
        f"Кнопка нажата\n\n"
        f"Имя: {user.first_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}"
    )

    await callback.message.answer("Подожди секунду… 🌷")
    await asyncio.sleep(2)

    await callback.message.answer_video(
        VIDEO_ID,
        caption="Иногда чужие слова говорят то, что я чувствую ❤️"
    )
    await asyncio.sleep(120)
    
    await callback.message.answer_photo(
    PHOTO_ID,
    caption="А это момент из сегодняшнего дня.\n\nПусть у нас всегда будет такая искра, как на этом фото ❤️"
    ) 

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Это для тебя, Кис")
    ])

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())