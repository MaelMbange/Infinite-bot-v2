import os
import discord
from discord.ext import commands
from InfiniteForm import *


token = os.getenv("INFINITE_BOT_TOKEN")
if token is not None:
    print("Token found !")
else:
    print("Token not found !")
    exit()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="@",intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#=====================================SPECIFIC-FUNCTIONS=====================================================

async def get_dm_channel(message):
    dm =  await message.author.create_dm()
    return dm

async def send_private(message, content:str):    
    async with message.typing():  
        dm_channel =  await get_dm_channel(message)
        await dm_channel.send(content)


async def send_image_private(message, image):
	dm_channel = await message.author.create_dm()
	await dm_channel.send(file=image)


async def clear_private(message):
    dm_channel = await get_dm_channel(message)
    async for message in dm_channel.history(limit=None):
        if message.author == bot.user:
            await message.delete()

async def send_medal(message, gamertag:str=None):
    #if gamertag is None: gamertag = message.author.name => aller chercher info fichier     
    img = Medal(gamertag)
    content = img.retrieve_image()
    async with message.typing(): await send_image_private(message, discord.File(content, filename=f"{gamertag}_medals.png"))

#========================================COMMAND-FUNCTIONS===================================================
@bot.command(name="start")
async def start(message, gamertag:str=None):
    print("start")
    print(gamertag)
    await send_medal(message, gamertag)


@bot.command(name="stop")
async def stop(message):
    print("stop")


@bot.command(name="register")
async def register(message, gamertag:str=None):
    print("register")


@bot.command(name="sayMyName")
async def sayMyName(message):
    print("sayMyName")


@bot.command(name="global")
async def global_stats(message, gamertag:str=None):
    print("global_stats")


@bot.command(name="lastGame")
async def last_game_stats(message, gamertag:str=None):
    print("last_game_stats")


@bot.command(name="clear")
async def clear(message):
    print("clear")

#============================================================================================================

bot.run(token)