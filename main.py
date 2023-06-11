# This example requires the 'message_content' intent.

import discord

# Priveledged gateway intent needs to read messages, this is set in the developer portal
intents = discord.Intents.default()
intents.message_content = True

# Connection to discord
client = discord.Client(intents=intents)

# Register event on ready, show that we've logged in


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Register event onmessage


@client.event
async def on_message(message):
    # Ignore ourselves
    if message.author == client.user:
        return
    # Anyone else says something beginning with "hello"
    if message.content.startswith('$hello'):
        print('hello detected')
        await message.channel.send('Hello!')


@client.event
async def on_message(message):
    # Ignore ourselves
    if message.author == client.user:
        return
    # Check if the message is a command to get the timestamp of the last message from a non-bot user
    if message.content == '!last_message_timestamp':
        # Get the channel object where the command was executed
        channel = message.channel

        # Get the last message in the channel
        last_message = await channel.fetch_message(channel.last_message_id)

        # Check if the last message is from a non-bot user
        if not last_message.author.bot:
            # Get the timestamp of the last message
            last_message_timestamp = last_message.created_at
            await message.channel.send(f"The last message from a non-bot user was posted at: {last_message_timestamp}")
        else:
            await message.channel.send("No recent message from a non-bot user found.")

# Run with the bot login token
