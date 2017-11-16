import discord
import asyncio
import random


client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name="try d!help"))



@client.event
async def on_message(message):
	if(message.author.id == '247852652019318795'):
		await client.delete_message(message)

client.run('MzgwODQ3Nzg2OTc2ODcwNDEx.DO-lUw.MbS-5sLWySijrdfynLM1YfEgOgg')
