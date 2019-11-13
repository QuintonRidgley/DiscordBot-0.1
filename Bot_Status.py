#Bot_Status.py
#Set to show the Command Prefix as a status

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Help | . for commands'))

client.run('MY_TOKEN')