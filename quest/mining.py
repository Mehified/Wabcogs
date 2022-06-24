import asyncio
import random
import discord
import calendar

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

from .data import Database

class Mining(commands.Cog):
    """
   Mining module
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.command()
    async def mine(self, ctx):
        """mining"""

        oreList = ["stone", "coal", "copper", "iron", "silver", "gold", "platinum", "titanium", "diamond"]
        oreProb = [0.9, 0.7, 0.55, 0.5, 0.4, 0.25, 0.15, 0.1, 0.05, 0.005]
        mineResult = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mineAttempt = 0
        
        await ctx.send("Mining...")
        
        embed = discord.Embed(colour=0xFF00FF, description="__Result__")
        embed.set_thumbnail(url='https://i.imgur.com/UioE5ls.png')
        embed.add_field(name = "stone", value = "1")
        '''
        for ore in oreList:
            mineAttempt = random()
            if mineAttempt < oreProb[ore]:
                mineResult[ore] += 1
                embed.add_field(name = oreList[ore], value = "1")
        '''
        return ctx.send(embed=embed)