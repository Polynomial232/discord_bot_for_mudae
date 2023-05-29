from DiscordBot import DiscordBot

class Mudae:
    def __init__(self, token, channel_id):
        self.name = 'mudae'
        self.value = 50
        self.discord = DiscordBot(token, channel_id)
        self.current_message_id = None

    def set_message(self, message):
        self.message = message

    def set_current_message_id(self, message_id):
        self.current_message_id = message_id

    def get_embeds(self):
        return self.message.get('embeds')
    
    def get_message_id(self):
        return self.message.get('id')
    
    def get_interact(self):
        message_id = self.get_message_id()
        author_id = self.message.get('author').get('id')
        components = self.message.get('components')[0].get('components')[0]

        return message_id, author_id, components
    
    def get_character_name(self):
        try:
            return self.get_embeds()[0].get('author').get('name')
        except:
            return None
    
    def get_character_value(self):
        return self.get_embeds()[0].get('description').split('**')[1]

    def is_mudae_message(self):
        return self.message.get('author').get('username').lower() == self.name.lower()

    def message_type(self):
        embeds = self.get_embeds()
        if embeds != [] and embeds[0].get('type') == 'rich':
            if embeds[0].get('footer') is None:
                return  'gacha'
            return 'detail'
        return None
    
    def next_event(self, type_message):
        if self.current_message_id != self.get_message_id(): 
            self.set_current_message_id(self.get_message_id())

            if type_message == 'gacha':
                self.discord.send_message(f"$im {self.get_character_name()}")
            
            if type_message == 'detail':
                value = self.get_character_value()
                print(value)
                if int(value) > self.value:
                    return value
                return value
        
        return None
