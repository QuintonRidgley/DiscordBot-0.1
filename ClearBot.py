#Clear Bot
#A simple command for Clearing Text channels
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('Bot is ready.')

@client.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10): 
	await ctx.channel.purge(limit=amount)

client.run('MY_TOKEN')