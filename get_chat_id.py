import requests

BOT_TOKEN = "8101949667:AAEglkb--2k--K7eiUQ-H1toM4xZ72GVhGs"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)
print(f"Status Code: {response.status_code}")
print("Full response:")
print(response.text)

# Try to extract chat_id
data = response.json()
if "result" in data and len(data["result"]) > 0:
    chat = data["result"][-1]["message"]["chat"]
    print(f"\nChat Title: {chat.get('title', 'N/A')}")
    print(f"Chat ID: {chat['id']}")
else:
    print("No messages found. Please send a message in the group.")