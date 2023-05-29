import requests
import json
import time

class DiscordBot:
    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        self.headers = { 'authorization': token }
    
    def send_message(self, message):
        payload = {"content": message}
        r = requests.post(self.url, data=payload, headers=self.headers)
        time.sleep(1)

        return r.status_code
    
    def get_messages(self):
        r = requests.get(self.url, headers=self.headers)
        messages_json = json.loads(r.text)

        return messages_json
    
    def interactions(self, message_id, author_id, components):
        url = 'https://discord.com/api/v9/interactions'
        payload = {
            "type": 3,
            # "nonce": "1112606271996952576",
            "guild_id": components.get('custom_id').split('p')[1],
            "channel_id": self.channel_id,
            "message_flags": 0,
            "message_id": message_id,
            "application_id": author_id,
            "session_id": "02617e8207cbe7f79e1c24afeb003ad9",
            "data": {
                "component_type": components.get('type'),
                "custom_id": components.get('custom_id')
            }
        }

        r = requests.post(url, json=payload, headers=self.headers)

        return r.status_code