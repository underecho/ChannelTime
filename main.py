#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 
import asyncio
from discord.ext import commands
from cogs import loops 

prev_time = 0
timeChannel = []

TOKEN = os.environ["TOKEN"]

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix="huiogdfsihugdfshuipfsgdihupdfsiphudsgfihup")

@bot.event
async def on_ready():
    await init()

async def init():
        global timeChannel
        c = {}
        for guild in bot.guilds:
            for j in guild.categories:
                if j.name == "🕐 SERVER TIME":
                    c[guild] = j

        ch = bot.get_all_channels()
        for i in ch:
            if i.category in c.values:
                await i.delete()
        for temp in bot.guilds:
            overwrites = {
                temp.default_role: discord.PermissionOverwrite(read_messages=True, connect=False),
                temp.me: discord.PermissionOverwrite(read_messages=True, connect=False)
            }
            timeChannel.append(await guild.create_voice_channel('Time', overwrites=overwrites, category=c[temp]))
        loops.setup(bot, timeChannel)
       
bot.run(TOKEN)