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

	messageType = random.randrange(0,10)

	if(message.author.id != client.user.id):
		if(messageType == 0):
			await client.send_message(message.channel, 'You were an accident ' + message.author.display_name + '.')
		elif(messageType == 1):
			await client.send_message(message.channel, 'Call me Bob Ross on anticonvulsants, because I just found a sad little accident.')
		elif(messageType == 2):
			await client.send_message(message.channel, 'You are in the 0.01 percent, because with you, the condom broke.')
		elif(messageType == 3):
			await client.send_message(message.channel, 'Hey ' + message.author.display_name + '!')
			await client.send_message(message.channel, "I'm talking to you Mr. Unwanted Child!")
		elif(messageType == 4):
			await client.send_message(message.channel, "Your mom won't have sex with me because she \"dosen't want annother accident like " + message.author.display_name + '".')
		elif(messageType == 5):
			await client.send_message(message.channel, 'What is it with failed abortions and clingyness?!?')
		elif(messageType == 6):
			await client.send_message(message.channel, 'Who knew that there could be an accident worse than Ajit Pai, but here you are...')
		elif(messageType == 7):
			await client.send_message(message.channel, "Hi accident, I'm Dad!")
		elif(messageType == 8):
			await client.send_message(message.channel, 'You take the phrase "Mistakes are human" to a literal level.')
		elif(messageType == 9):
			await client.send_message(message.channel, 'You are the reason I am pro-choice.')
			await client.send_message(message.channel, 'Who could be pro-life with a failure like you.')


client.run('MzgwODQ3Nzg2OTc2ODcwNDEx.DO-lUw.MbS-5sLWySijrdfynLM1YfEgOgg')
