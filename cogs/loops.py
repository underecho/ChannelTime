import os
import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime, timedelta, timezone

prev_time = 0
GUILD_ID = int(os.environ["GUILD_ID"])
CATEGORY_ID = int(os.environ["CATEGORY_ID"])
MES = os.environ["MES"]

class loops(commands.Cog):

    def __init__(self, bot, timeChannel):
        self.bot = bot
        self.timeChannel = timeChannel
        self.loops.start()

    @tasks.loop(seconds=5)
    async def loops(self):
        global prev_time
        # 現在の時刻
        emoji = bot.emoji
        JST = timezone(timedelta(hours=+9), 'JST')
        now = datetime.now(JST).strftime('%m/%d - %H:%M')
        if now != prev_time:
            text = f"🕒 {now}(JST)"
            await self.timeChannel.edit(name=text)


def setup(bot, timeChannel):
    bot.add_cog(loops(bot, timeChannel))


