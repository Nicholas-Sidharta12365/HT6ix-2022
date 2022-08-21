from venv import create
import discord
import os
from dotenv import load_dotenv
from bot_database import create_db, log_message, get_all_messages_past_x_hours
from datetime import datetime
import math
import openai
import numpy as np
import asyncio
from cohere_engine import generate, classify
from numpy_preprocess import adapt_array
from mood_time_series import predict_mood

load_dotenv()
MOOD = ['sad', 'angry', 'curious', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised']
HOURS = 2


def get_gpt3_message(message):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    data = openai.Completion.create(
        model="text-davinci-002",
        prompt=message,
        max_tokens=100,
        temperature=0
    )
    return data.to_dict()["choices"][0]["text"].strip("\n")

MOOD = ['sad', 'angry', 'curious', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised']

def suggest_activity(author_id):
    messages = get_all_messages_past_x_hours(author_id, HOURS)
    data = [message[2] for message in messages]
    # print(data)
    moods, prediction = predict_mood(data)
    idx = (-moods).argsort()[:3] #indices of largest to smallest
    moods_top_3 = [MOOD[i] for i in idx]
    ret_messages = []
    for mood in moods_top_3:
        if mood not in ["curious", "neutral", "surprised"]:
            ret_messages.append(get_gpt3_message(f"Write a suggestion to promote mental health for a worker who is feeling {mood} while at work"))
    return ret_messages

def apply_sigmoid(message):
    return (2.5 / (1 + np.exp(-(message[1]-2/3*HOURS*3600)/(HOURS*3600/16))))*message[2]

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

            if message.content.startswith('!mood'):
                messages = get_all_messages_past_x_hours(str(author_id), HOURS) # returns a list of messages, more recent = bigger value for message[1]
                data = [apply_sigmoid(msg) for msg in messages]
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
                await message.channel.send(embed=embed, content=None)
            elif message.content.startswith("!suggest"):
                bot_msg = await message.channel.send("Mental Health Bot is thinking...")
                messages = suggest_activity(author_id)
                embed_options = {"title": f"Mental Health Suggestions", "type": "rich", "color": 2899536, "timestamp": str(datetime.utcnow())}
                embed = discord.Embed.from_dict(embed_options)
                for i, msg in enumerate(messages):
                    embed.add_field(name=f"Suggestion {i+1}", value=msg)
                await bot_msg.edit(embed=embed, content=None)
            else:
                create_db(str(author_id)) # can log existing users a do a check if that user exists
                time_count = datetime.now() - datetime(2022, 8, 19, 0, 0, 0)
                second_count = math.floor(time_count.total_seconds())
                # print(second_count)
                classification = classify(message.content)
                # print(classification)
                log_message(str(author_id), message.content, second_count, adapt_array(classification))


def main():
    client = MyClient()
    client.run(os.getenv('TOKEN'))
    # openai.organization = "org-egOUH3FiN9wJSzhHqGGRoZXO"
    openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':
    main()