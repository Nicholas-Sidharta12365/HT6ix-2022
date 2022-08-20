from venv import create
import discord
import os
from dotenv import load_dotenv
from bot_database import create_db, log_message, get_all_messages_past_x_hours
from datetime import datetime
import math
import requests
import json

load_dotenv()

# def get_messages(author_id, x):
#     return get_all_messages_past_x_hours(author_id, x)
class MyClient(discord.Client):
    def __init__(self, intents=discord.Intents.default()):
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(dir(message), message.author, message.content)
        if message.author != self.user:
            author_id = message.author.id
            create_db(str(author_id)) # can log existing users a do a check if that user exists
            time_count = datetime.now() - datetime(2022, 8, 19, 0, 0, 0)
            second_count = math.floor(time_count.total_seconds())
            # print(second_count)
            log_message(str(author_id), message.content, second_count) #more recent ones are at the top
            print(get_all_messages_past_x_hours(str(author_id), 3)) # returns a list of messages

def main():
    client = MyClient()
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()