#working baseline
#all this does is prints into the terminal saying that the Bot has a successful link

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')

client.run('MY_TOKEN')
