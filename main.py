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
                if j.name == "🕐 Server Time":
                    c[guild.id] = j.id
        else:
            for a in bot.guilds:
                try:
                    print(f"founded:{c[a.id]}")
                except:
                    uiu = await a.create_category("🕐 Server Time")
                    c[a.id] = uiu.id
                for i in a.voice_channels:
                    if i.type ==  discord.ChannelType.voice:
                        if i.category_id == c[i.guild.id]:
                            await i.delete()

        for temp in bot.guilds:
            overwrites = {
                temp.default_role: discord.PermissionOverwrite(read_messages=True, connect=False),
                temp.me: discord.PermissionOverwrite(read_messages=True, connect=False)
            }
            print(type(c[temp.id]))
            try:
                timeChannel.append(await temp.create_voice_channel('Time', overwrites=overwrites, category=bot.get_channel(c[temp.id])))
            except:
                print("error")
        loops.setup(bot, timeChannel)

bot.run(TOKEN)