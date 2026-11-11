# Moliya Pro — Telegram Mini App & Bot

Faqat ruxsat berilgan 2 ta akkaunt (ID: `7789172387`, `8622259094`) uchun maxsus shaxsiy moliya boshqaruv tizimi.

## 📁 Tarkibi
1. `index.html` — Yuqori darajadagi Obsidian Dark / Glassmorphism interfeysli Telegram Mini App.
2. `bot.py` — Aiogram 3 da yozilgan, begonalar kirmaydigan server boti.
3. `Dockerfile` va `docker-compose.yml` — Serverda konteynerda ishlatish uchun.
4. `deploy.sh` — Ubuntu/Debian serverida 1 ta komanda bilan o'rnatish.
5. `requirements.txt` — Python kutubxonalari.

## 🚀 GitHub va Serverga O'rnatish

### 1-qadam: GitHub Pages (Mini App uchun)
1. GitHub-da yangi `moliya-pro` nomli ochiq (public) repozitoriya oching.
2. Ushbu arxivdagi barcha fayllarni yuklang (`git push`).
3. Repozitoriya sozlamalariga kiring: **Settings -> Pages**.
4. **Branch**: `main` va papka `/root` qilib **Save** tugmasini bosing.
5. GitHub sizga havola beradi (masalan: `https://username.github.io/moliya-pro`).
6. O'sha linkni `bot.py` ichidagi `WEB_APP_URL` qatoriga yozib qo'ying.

### 2-qadam: Serverda Ishga Tushirish (VPS / Linux)
Terminalda quyidagi 1 ta komandani bering:
```bash
bash deploy.sh
```
Yoki Docker orqali:
```bash
docker compose up -d --build
```
