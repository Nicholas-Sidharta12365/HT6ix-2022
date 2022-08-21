# IntelliCord

<img src="landing/public/images/pfp.png">

## Developed by
### Alfonsus Rodriques Rendy | Kevin Qu | Nicholas Sidharta

## About
### IntelliCord is a discord bot that purposes as a mental health tracker and gives out solutions / support to the user based on the current mental state

##Setup
Create a Discord bot at https://discord.com/developers/applications and give it permissions to read, write, edit and send messages at least

Set up an account at https://cohere.ai/ and https://beta.openai.com/

Create a `.env` file in the root directory with `TOKEN=YOUR_DISCORD_TOKEN` and `OPENAI_API_KEY=YOUR_OPEN_AI_KEY`

You can use your own co:here classification model by changing the model in `cohere_engine.py`

Run `pip install -r requirements.txt` to install all Python requirements

Run `python bot.py` to start the discord bot

##Website

Instructions to launch the website are in `landing/`
