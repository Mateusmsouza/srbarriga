from os import getenv

import requests


def send_message(message: str):
    api_telegram = getenv("API_TELEGRAM")
    bot_key = getenv("BOT_KEY")
    chat_id = getenv("CHAT_ID")
    requests.get(
        url=f"{api_telegram}/bot{bot_key}/sendMessage?chat_id={chat_id}&text={message}"
    )
