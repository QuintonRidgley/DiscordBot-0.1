#Kick/Ban.py
#Use Case: intering a commond instead of finding user, clicking ban
#just a little easier for moblie to use command.

import os
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print ('has connected to Discord!')

@client.command(name='kick')
@commands.has_permissons(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@client.command(name='ban')
@commands.has_permissons(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

client.run('MY_TOKEN')