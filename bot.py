import asyncio
import json
import logging
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = "8824955083:AAF5Vvs-ihI026VbVX698NzIZM5g9TFaMk8"
ALLOWED_IDS = {7789172387, 8622259094}
WEB_APP_URL = "https://umaaarov77-maker.github.io/moliya-pro/"

REMINDERS_FILE = "reminders.json"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def load_reminders():
    if os.path.exists(REMINDERS_FILE):
        try:
            with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_reminders(data):
    with open(REMINDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    if user_id not in ALLOWED_IDS:
        await message.answer("🔒 Kechirasiz, ushbu tizim faqat maxsus hisob egalari uchun yopiq rejimda ishlaydi.")
        return

    first_name = message.from_user.first_name or "Mijoz"
    kb = InlineKeyboardMarkup(
      inline_keyboard=[[InlineKeyboardButton(text="⚡ Moliya Pro-ni Ochish", web_app=WebAppInfo(url=WEB_APP_URL))]]
    )

    await message.answer(
        f"Assalomu alaykum, {first_name}!\n\n"
        "Moliya Pro tizimiga xush kelibsiz. Hisob-kitoblar, kunbay xarajatlar va qarz muddatlari nazoratingizda.",
        reply_markup=kb
    )

# Mini App'dan yuborilgan eslatmalarni qabul qilish
@dp.message(F.web_app_data)
async def web_app_handler(message: Message):
    user_id = message.from_user.id
    if user_id not in ALLOWED_IDS:
        return

    try:
        data = json.loads(message.web_app_data.data)
        if data.get("action") == "set_debt_reminder":
            reminders = load_reminders()
            reminders.append({
                "user_id": user_id,
                "title": data.get("title"),
                "amount": data.get("amount"),
                "due_date": data.get("dueDate"),
                "notified": False
            })
            save_reminders(reminders)
            await message.answer(
                f"⏰ **Qarz eslatmasi saqlandi!**\n\n"
                f"👤 Izoh: {data.get('title')}\n"
                f"💰 Summa: {data.get('amount'):,} UZS\n"
                f"📅 Qaytarish sanasi: {data.get('dueDate')}\n\n"
                "Kuni kelganda sizga eslatma xabarini yuboraman."
            )
    except Exception as e:
        logging.error(f"Eslatma saqlashda xato: {e}")

# Har 1 soatda qarzlarni tekshirib eslatma yuboruvchi fon xizmati
async def check_debt_reminders():
    while True:
        try:
            today_str = datetime.now().strftime("%Y-%m-%d")
            reminders = load_reminders()
            updated = False

            for item in reminders:
                if not item.get("notified") and item.get("due_date") == today_str:
                    text = (
                        f"🔔 **DIQQAT: Qarz qaytarish kuni keldi!**\n\n"
                        f"📌 Izoh: {item.get('title')}\n"
                        f"💵 Summa: {item.get('amount'):,} UZS\n\n"
                        f"Iltimos, qarz holatini tekshirib, Mini App orqali belgilab qo'ying."
                    )
                    try:
                        await bot.send_message(chat_id=item["user_id"], text=text, parse_mode="Markdown")
                        item["notified"] = True
                        updated = True
                    except Exception as err:
                        logging.error(f"Xabar yuborishda xato: {err}")

            if updated:
                save_reminders(reminders)
        except Exception as e:
            logging.error(f"Eslatma siklida xato: {e}")

        await asyncio.sleep(3600)  # Har 1 soatda tekshiradi

async def main():
    asyncio.create_task(check_debt_reminders())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
