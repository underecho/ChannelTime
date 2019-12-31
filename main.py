#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 
import asyncio
from discord.ext import commands
from cogs import loops 

prev_time = 0
GUILD_ID = int(os.environ["GUILD_ID"])
CATEGORY_ID = int(os.environ["CATEGORY_ID"])
MES = os.environ["MES"]
timeChannel = None

TOKEN = os.environ["TOKEN"]

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix="huiogdfsihugdfshuipfsgdihupdfsiphudsgfihup")

@bot.event
async def on_ready():
    await init()

async def init():
        global timeChannel
        guild = bot.get_guild(GUILD_ID)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=False)
        }
        c = bot.get_channel(CATEGORY_ID)
        ch = bot.get_all_channels()
        for i in ch:
            if i.category == c:
                await i.delete()

        timeChannel = await guild.create_voice_channel('Time', overwrites=overwrites, category=c)
        await guild.create_voice_channel(MES, overwrites=overwrites, category=c)
        loops.setup(bot, timeChannel)
       
bot.run(TOKEN)