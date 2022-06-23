import asyncio
import random
import discord
import calendar

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config
from redbot.core.utils.predicates import MessagePredicate

from .data import Database

account_defaults = {
    "Level": 1,
    "HP": 10,
    "Stamina": 100,
    "STR": 1,
    "AGI": 1,
    "INT": 1,
    "END": 1,
    "Inventory": { },
    "Money": { },
    "Materials": { },
}

class Quest(commands.Cog):
    """
   Small text-based RPG.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.command()
    async def queststart(self, ctx):
        """Creates account for quest RPG"""
        await ctx.send("Account created!")

    @commands.command()
    async def account(self, ctx):
        """Creates account for quest RPG"""
        embed = discord.Embed(colour=0xFF0000, description="Test")
        embed.set_thumbnail('https://i.imgur.com/UioE5ls.png')
        #embed.add_field(name=_("{}'s Profile").format(ctx.author.name)), value="l0l",
        #embed.add_field(name="__Stats__", value=account_defaults)
        embed.set_footer(text=_("heya"))
        await ctx.send(embed=embed)