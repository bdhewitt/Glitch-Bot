#Glitch Bot by Dr-Chrono

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import re

client = discord.Client()
bot = commands.Bot(command_prefix='#')

@bot.event
async def on_message(message):
    await poorsucker(message)
    await bot.process_commands(message)

#Lets me see when the bot is ready
@bot.event
async def on_ready():
    print ("time for you to go to bed!")
    print ("Logged in as " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    print ("----------")

@bot.event
async def on_server_join(ser):
    await bot.send_message(ser.default_channel, "Hi {}, I\'m Glitchbot! I will make sure that you go to bed on time".format(ser.nam))


async def poorsucker(message):
        if message.author != message.server.me:
            word = re.search(r'\bi\'?m\s+(.*)', message.contant, re.IGNORECASE)
        if word is not None:
            if len(word.group(1)) > 32:
                word = re.search(r'\bi\'?m\s+(\w+)', message.content, re.IGNORECASE)
            word = word.group(1)
        else:
            await client.send_message(message.channel, str(message.author.mention))
            await bot.send_message(message.channel, "YOU SHOULD BE IN BED!")

@bot.command(pass_context=True)
async def glitchbot(ctx):
    await bot.raw_mentions("You should be sleeping. GO TO BED! =/")

bot.run("NDY2MzczMDg2Nzk1NzkyMzk3.DibHbw.bezdV7WAjGhKXmgpQAiTnq5xpEo")