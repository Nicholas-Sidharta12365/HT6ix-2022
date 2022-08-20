import discord
import os
from dotenv import load_dotenv
import requests
import json
from cohere_engine import generate

load_dotenv()

intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('piece of garbage'):
        response = generate(['piece of garbage'])
        await message.channel.send(response)

client.run(os.getenv('TOKEN'))