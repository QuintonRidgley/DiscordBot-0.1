# Minimal.py
# Quinton Ridgley
import os
import discord
from gotnev import load_dotnev

load_dotnev()
token = os.getenv('Your_Token_Here')

client = discord.Client()

@client.event
async def on_ready():
	print (f'{client.user} has connected to Discord!')

client.run(token)
