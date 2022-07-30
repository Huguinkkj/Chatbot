import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

@client.event
async def on_ready():
    print(f"The {client.user} is ready, babe")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if message.author == client.user:
        return
    if message.content.startswith('$ai'):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

client.run('MTAwMjI3ODczNjk2MTQ3NDY0MA.Gcsn_6.jqpJi5lzL7XNMTY6WVC1AoFBLJFeL7Qq9V-APQ')
