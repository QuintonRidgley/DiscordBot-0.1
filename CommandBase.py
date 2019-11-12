#CommandBase.py
#all this does it pings the bot (will add f'...ms' at some point)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MY_TOKEN')