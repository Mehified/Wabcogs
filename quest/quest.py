from typing import Literal

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

import discord

class Quest(commands.Cog):
    """
   Small text-based RPG.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=quest,
            force_registration=True,
        )

    @commands.command()
    async def queststart(self, ctx):
        """Creates account for quest RPG"""
        await ctx.send("Account created!")
