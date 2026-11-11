#!/bin/bash
# VPS Serverda bir buyruq bilan ishga tushirish skripti
echo "=== Moliya Pro Serverni Ishga Tushirish ==="
sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv git screen

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Bot fonda (background screen orqali) ishga tushirilmoqda..."
screen -dmS moliya_bot python3 bot.py

echo "Tayyor! Bot serverda uzluksiz ishlamoqda."
