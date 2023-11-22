# 必要モジュールのインポート
import os
import requests, json
from dotenv import load_dotenv

class DiscordNotification:
    def __init__(self):
        load_dotenv()

    def __create_message(self):
        message  =  "**定期報告の時間です**\n\n"
        message +=  "定期報告の時間になりました。\n"
        message +=  "現在の進捗を報告して下さい。\n\n"
        message +=  "**記述例**\n"
        message +=  "> 1. 完成させた機能\n"
        message +=  "> （完成させた機能を記述。承認後のPullRequestsのURLもあると良い。）\n"
        message +=  "> 2. 現在取り組んでいること\n"
        message +=  "> （今完成していなくても良い。完成予定日があると良い。）\n"
        message +=  "> 3. 現在の問題点・相談\n"
        message +=  "> （具体的な問題点を記述する。どうしたいのか、どうして欲しいのかがあると良い。）\n\n"
        message +=  "**関連URL**\n"
        message +=  "* Githubリポジトリ\n"
        message += f"  * {os.environ['GITHUB_URL']}\n"
        message +=  "* Github Projects Develop\n"
        message += f"  * {os.environ['PROJECT_DEV_URL']}\n"
        message +=  "* Github Projects プロダクトバックログ\n"
        message += f"  * {os.environ['PROJECT_PBI_URL']}\n"
        message +=  "* Scrapbox\n"
        message += f"  * {os.environ['SCRAPBOX_URL']}\n"
        message +=  "* Tely\n"
        message += f"  * {os.environ['PRODUCT_URL']}\n"

        return message

    def send_message(self):
        webhook_url  = os.environ['DISCORD_WEBHOOK_URL']
        main_content = {
                        "username": os.environ['BOT_NAME'],
                        "avatar_url": os.environ['BOT_AVATAR_URL'],
                        "content": self.__create_message()
                    }
        
        headers = {"Content-Type": "application/json"}

        response = requests.post(webhook_url, json.dumps(main_content), headers=headers)