import os
import requests

URL = "https://www.darty.com/nav/extra/list?seller=311290-311291-311289-327183-328771-311452-0&cat=420"

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"}).text

if "BTU" in page or "climatiseur" in page.lower():
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "🚨 Vérification Darty effectuée. Des climatiseurs sont présents sur la page : https://www.darty.com/nav/extra/list?seller=311290-311291-311289-327183-328771-311452-0&cat=420"
        },
    )
