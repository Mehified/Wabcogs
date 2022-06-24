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
   Small text-based RPG.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.command()
    async def mine(self, ctx):
        """mining"""
        
        #check stamina
        oreList = ["stone", "coal", "copper", "iron", "silver", "gold", "platinum", "titanium", "diamond"]
        oreProb = [0.9, 0.75, 0.55, 0.5, 0.4, 0.25, 0.15, 0.1, 0.05, 0.005]
        mineResult = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mineAttempt = 0
        
        
        embed = discord.Embed(colour=0xFF0000, description="__Result__")
        embed.set_thumbnail(url='https://i.imgur.com/UioE5ls.png')
        for ore in oreList:
            mineAttempt = rand(0, 1)
            if mineAttempt < oreProb[ore]:
                mineResult[ore] = 1
                embed.add_field(name = oreList[ore], value = str(mineResult[ore])
        
        await ctx.send(embed=embed)