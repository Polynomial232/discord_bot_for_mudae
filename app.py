from decouple import config
from Mudae import Mudae
import time

TOKEN = config('TOKEN')
CHANNEL_ID_PRIVATE = config('CHANNEL_ID_PRIVATE')
CHANNEL_ID = config('CHANNEL_ID')

private_bot = Mudae(token=TOKEN, channel_id=CHANNEL_ID_PRIVATE)
bot = Mudae(token=TOKEN, channel_id=CHANNEL_ID)

while True:
    message = bot.discord.get_messages()
    bot.set_message(message)
    
    message_private = private_bot.discord.get_messages()
    private_bot.set_message(message_private)

    if bot.is_mudae_message():
        if bot.message_type() == 'gacha' and bot.get_character_name() != private_bot.get_character_name():
            private_bot.set_message(message)
            private_bot.next_event('gacha')
        
        if private_bot.message_type() == 'detail':
            bot.set_message(message_private)
            bot.next_event('detail')
        
        private_bot.set_message(message_private)
    else:
        print("Not")

    time.sleep(0.3)