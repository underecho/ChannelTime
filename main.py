#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

prev_time = 0
timeChannel = None

TOKEN = os.environ["TOKEN"]
GUILD_ID = int(os.environ["GUILD_ID"])
CATEGORY_ID = int(os.environ["CATEGORY_ID"])
MES = os.environ["MES"]
# 接続に必要なオブジェクトを生成
client = discord.Client()

@tasks.loop(seconds=5)
async def loop(channel):
    global prev_time
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now != prev_time:
        await channel.edit(name=now)

#ループ処理実行
@client.event
async def on_ready():
    await init()

async def init():
    global timeChannel
    guild = client.get_guild(GUILD_ID)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=False)
    }
    c = await client.get_channel(CATEGORY_ID)
    ch = await client.get_all_channels()
    for i in ch:
        if i.category == c:
            i.delete()

    timeChannel = await guild.create_text_channel('Time', overwrites=overwrites, category=c)
    await guild.create_text_channel(MES, overwrites=overwrites)

loop.start(timeChannel)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)