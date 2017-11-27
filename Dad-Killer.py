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
	await client.change_presence(game=discord.Game(name="your mom"))



@client.event
async def on_message(message):

	messageType = random.randrange(0,3)

	if(message.author.id != client.user.id):
		if(messageType == 0):
			await client.send_message(message.channel, 'You were an accident ' + message.author.display_name)
		elif(messageType == 1):
			await client.send_message(message.channel, 'Call me Bob Ross on anticonvulsants, because I just found a sad little accident')
		elif(messageType == 2):
			await client.send_message(message.channel, 'You are in the 0.01 percent, because with you, the condom broke')

client.run('MzgwODQ3Nzg2OTc2ODcwNDEx.DO-lUw.MbS-5sLWySijrdfynLM1YfEgOgg')
