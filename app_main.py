from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "FairDeal Bot is Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)

    # Extract from TradingView alert payload
    symbol = data.get('symbol', 'Unknown')
    side = data.get('side', 'N/A')
    timeframe = data.get('timeframe', 'N/A')
    note = data.get('note', '📢 TradingView Alert')

    # Formatted Telegram message
    message = f"""
🚨 {side} Signal on {symbol}
🕒 Timeframe: {timeframe}
📝 Note: {note}
"""

    # Telegram Bot credentials
    BOT_TOKEN = "8101949667:AAEglkb--2k--K7eiUQ-H1toM4xZ72GVhGs"
    CHAT_ID = "-1002528960448"

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    # Send to Telegram
    response = requests.post(telegram_url, json=payload)
    print("Telegram response:", response.text)

    return f"✅ Sent message:\n{message}", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0",port=port)
