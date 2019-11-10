import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
		
@client.event
async def on_message(Message):
	if message.author == client.user:
		return
		
	if message.content.startswith('$hello'):
		await message.channel.send ('Hello!')

client.run ('NjQzMTQ0NjIwNDYwNzM2NTEy.XchNWA.avK09lwFcGY6WTuX3w8l-E5pu6U')
