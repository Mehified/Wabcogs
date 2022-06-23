import asyncio
import discord
import copy

from redbot.core import Config
from redbot.core.bot import Red
#from redbot.core.config import Config
from redbot.core.utils.predicates import MessagePredicate

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

class Database

    def __init__(self):
        self.config.register_account(**account_defaults)
        self.cog_ready_event: asyncio.Event = asyncio.Event()
        
    async def get_data(self, ctx, player=None):
        if player is None:
            return self.config
        else:
            return self.config.user(player)
