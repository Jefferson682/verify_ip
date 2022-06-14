from dynaconf import settings
from datetime import datetime
import requests

def slack_notification(title, service, author, type, message):
    data = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{title}",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Service:*\n{service}"
                    },
                    {
                        "type": "mrkdwn",
                        # Change for your email
                        "text": f"*Created by:*\n<example.com|{author}>"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*When:*\n{datetime.now()}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Type:*\n{type}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Message:*\n{message}"
                }
            }
	]
}
    url = settings.SLACK_WEBHOOK_URL
    try:
        r = requests.post(url=url, json=data)
        print(r.text)
        return r
    except requests.exceptions as e:
        return e