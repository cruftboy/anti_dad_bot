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
	elif(message.author.id == '261185713779900427'):
		if('im' in message.content.lower()):
			name = message.content.lower()
			indexiam = name.find('im')
			name = name[(indexiam+2):]
			await client.send_message(message.channel, 'Hi' + name + ", i'm dad!")
		elif("i'm" in message.content.lower()):
			name = message.content.lower()
			indexiam = name.find("i'm")
			name = name[(indexiam+3):]
			await client.send_message(message.channel, 'Hi' + name + ", i'm dad!")

client.run('MzgwODQ3Nzg2OTc2ODcwNDEx.DO-lUw.MbS-5sLWySijrdfynLM1YfEgOgg')
