#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 
from discord.ext import commands
from cogs.

TOKEN = "" #トークン
CHANNEL_ID = "" #チャンネルID
# 接続に必要なオブジェクトを生成

bot = commands.Bot()

client = discord.Client()

@bot.event
async def on_ready():


client.run(TOKEN)