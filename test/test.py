import discord
import json

client = discord.Client()


def getToken():
    with open('key.json') as f:
        data = json.load(f)
        token = data["KEY"]
        return token


@client.event
async def on_ready():
    print('Login complete: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send('Hello')


key = getToken()
client.run(key)