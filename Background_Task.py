#Background_Task.py
#Cycles Playing status

import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['Help | . for commands', 'Status 2'])

#on_ready()
	change_status.start()

@task.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=dicord.Game(next(status)))

client.run('MY_TOKEN')