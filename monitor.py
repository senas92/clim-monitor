import requests
import hashlib
import os
import time

URL = "https://www.darty.com/nav/extra/list?seller=311290-311291-311289-327183-328771-311452-0&cat=420"

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(URL, headers=headers, timeout=20)
    return r.text

def main():
    old_hash = None

    while True:
        page = get_page()
        new_hash = hashlib.md5(page.encode()).hexdigest()

        if old_hash and new_hash != old_hash:
            send_message(
                "🚨 Changement détecté sur la page Darty Climatisation !\n\n"
                "Vérifie rapidement les nouveaux stocks."
            )

        old_hash = new_hash
        time.sleep(60)

if __name__ == "__main__":
    main()
