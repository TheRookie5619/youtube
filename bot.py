import discord

token = 'Ur_token'
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    user = str(message.author).split('#'[0])
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{user}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '!pong':
        await message.channel.send('Ping!')
    elif user_message.lower() == '!hello':
        await message.channel.send(f'Hello! {user}')
    # and so on