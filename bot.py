import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

# Bot konfiguratsiyasi
BOT_TOKEN = "8824955083:AAF5Vvs-ihI026VbVX698NzIZM5g9TFaMk8"

# Faqat ruxsat etilgan 2 ta akkaunt
ALLOWED_IDS = {7789172387, 8622259094}

# GitHub Pages yoki Vercel linki
WEB_APP_URL = "https://umaaarov77-maker.github.io/moliya-pro/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id

    # Xavfsizlik filtri: Begonalarni rad etish
    if user_id not in ALLOWED_IDS:
        await message.answer(
            "🔒 **Kirish cheklangan!**\n\n"
            "Ushbu moliyaviy tizim shaxsiy bo'lib, begonalar uchun bloklangan.",
            parse_mode="Markdown"
        )
        return

    # Asosiy egasi uchun interfeys
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚡ Moliya Pro-ni Ochish",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(
        f"Salom, **{message.from_user.first_name}**! 💎\n\n"
        "Shaxsiy moliya va xarajatlar nazorati tizimi xizmatingizga shay.\n"
        "Ilovani ishga tushirish uchun quyidagi tugmani bosing:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

async def main():
    print("Moliya Pro Boti serverda muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
