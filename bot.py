import discord
import os
import logging

# Logger setup
logging.basicConfig(level=logging.DEBUG)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.debug(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    logging.debug(f'Received message: {message.content}')

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Error handling
@client.event
async def on_error(event, *args, **kwargs):
    logging.error(f'Error in event {event}: {args[0]}', exc_info=True)

try:
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        raise ValueError("No token provided. Set the DISCORD_TOKEN environment variable.")
    client.run(TOKEN)
except Exception as e:
    logging.critical('Failed to start bot', exc_info=True)