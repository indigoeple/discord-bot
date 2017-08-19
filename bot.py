import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  
@client.event
async def on_message(message):
  if message.content.startswith('!shout'):
    await client.send_message(message.channel, 'SHOUT OUT LOUD!')

client.run('MzQ4MzQxMjUxNTU4MzQyNjc2.DHlwJg.Rlb1QsUhLjXbHCPc3q9YHj9KixQ')
