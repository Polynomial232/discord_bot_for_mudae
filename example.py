from DiscordBot import DiscordBot
from decouple import config

TOKEN = config('ENV')
CHANNEL_ID = config('channel_id')

private_bot = DiscordBot(token=TOKEN, channel_id=CHANNEL_ID)
private_bot.send_message('$w')
message = private_bot.get_messages()
character_name = message[0].get('embeds')[0].get('author').get('name')
private_bot.send_message(f'$im {character_name}')
message = private_bot.get_messages()
message_id = message[0].get('id')
author_id = message[0].get('author').get('id')
components = message[0].get('components')[0].get('components')[0]
interact = private_bot.interactions(message_id, author_id, components)