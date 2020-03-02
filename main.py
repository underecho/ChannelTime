#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 
import asyncio
from discord.ext import commands
from cogs import loops 

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
        for a in bot.guilds:
            for i in a.voice_channels:
                if i.name[0] == "🕒":
                    timeChannel.append(i)

        for temp in bot.guilds:
            overwrites = {
                temp.default_role: discord.PermissionOverwrite(read_messages=True, connect=False),
                temp.me: discord.PermissionOverwrite(read_messages=True, connect=False)
            }
            try:
                timeChannel.append(await temp.create_voice_channel('Time', overwrites=overwrites))
            except:
                print("error")
        loops.setup(bot, timeChannel)

bot.run(TOKEN)