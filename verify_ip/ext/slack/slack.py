import requests

def slack_notification(url, data):
    try:
        r = requests.post(url, json=data)
        return r
    except Exception as error:
        return error
    
