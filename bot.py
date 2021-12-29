import discord
import asyncio
import requests
import youtube_dl
import info_getter
from dotenv import load_dotenv
import os
client = discord.Client()

load_dotenv()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
# voice channel commands for youtube bot 
    elif message.content.startswith("$price"):
        print(message.content)
        list_of_coins = info_getter.list_of_cryptos()
        print(len(list_of_coins))

    elif message.content.startswith("!npos"):
        regex = "/,(?![^(]*\)) /"
        print(len(message.content))
        #regex not working but is the solution to the issue for pt array 
        message_array = message.content.split(regex)
        print(message_array)

    elif message.content.startswith('!play'):
        await message.channel.send('get lost nerdling !')
        print(message.author.voice)
        if message.author.voice != None: 
            await message.author.move_to(None)
        else:
            await message.channel.send("You are not in a voice channel")

token = os.getenv('DISCORD_API_KEY')
client.run(token)

