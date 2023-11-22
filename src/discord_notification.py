# 必要モジュールのインポート
import os
import requests, json
from dotenv import load_dotenv

class DiscordNotification:
    def __init__(self):
        load_dotenv()

    def __create_message(self):
        return "テスト"

    def send_message(self):
        webhook_url  = os.environ['DISCORD_WEBHOOK_URL']
        main_content = {
                        "username": os.environ['BOT_NAME'],
                        "avatar_url": os.environ['BOT_AVATAR_URL'],
                        "content": self.__create_message()
                    }
        
        headers = {"Content-Type": "application/json"}

        response = requests.post(webhook_url, json.dumps(main_content), headers=headers)