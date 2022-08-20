from venv import create
import discord
import os
from dotenv import load_dotenv
from bot_database import create_db, log_message, get_all_messages_past_x_hours
from datetime import datetime
import math
import requests
import json
import numpy as np
from cohere_engine import generate, classify
from numpy_preprocess import adapt_array
from mood_time_series import predict_mood

load_dotenv()
MOOD = ['sad', 'angry', 'curious', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised']

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
            classification = classify(message.content)
            # print(classification)
            log_message(str(author_id), message.content, second_count, adapt_array(classification))
            messages = get_all_messages_past_x_hours(str(author_id), 1) # returns a list of messages
            data = [message[2] for message in messages]
            # print(data)
            mood, prediction = predict_mood(data)
            # await message.channel.send(f"**{message.author}**, your mood right now: {mood}")
            # await message.channel.send(result[0])

            embedOptions = {
                "title": "Mood checker",
                "type": "rich",
                "color": 2899536,
                "description": f"**{message.author}'s** mood right now: {prediction}",
                "timestamp": str(datetime.utcnow())
            }
            
            embed = discord.Embed.from_dict(embedOptions)
            embed.add_field(name='\U0001F622', value=f'{round(mood[0] * 100)}%', inline=True)
            embed.add_field(name='\U0001F621', value=f'{round(mood[1] * 100)}%', inline=True)
            embed.add_field(name='\U0001F9D0', value=f'{round(mood[2] * 100)}%', inline=True)
            embed.add_field(name='\U0001F92E', value=f'{round(mood[3] * 100)}%', inline=True)
            embed.add_field(name='\U0001F628', value=f'{round(mood[4] * 100)}%', inline=True)
            embed.add_field(name='\U0001F600', value=f'{round(mood[5] * 100)}%', inline=True)
            embed.add_field(name='\U0001F610', value=f'{round(mood[6] * 100)}%', inline=True)
            embed.add_field(name='\U0001F62F', value=f'{round(mood[7] * 100)}%', inline=True)
            embed.add_field(name='** **', value='** **', inline=True)
            await message.channel.send(embed=embed)

def main():
    client = MyClient()
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()