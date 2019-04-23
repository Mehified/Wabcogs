from random import randint
from random import choice
from redbot.core import commands
from redbot.core import Config

import dateutil.parser
import discord

class Gacha(commands.Cog):
    """
    Plays a game of gachapon.
    """
    def __init__(self, bot):
        self.bot = bot


    def _convertList(self, rollList):
        #eventually move to outside of this file
        rarityTable = {
            "S": 10,
            "A": 500,
            "B": 2000,
            "C": 10000
        }
        dictS = {
            "gonface": {},
            "BlademasterX": {},
            "Varun's Mom": {},
            "Hoodrat Jordan": {},
            "Daughter Arta": {},
            "T-Time Cosplay Pat": {},
            "GAYM": {},
            "Roar": {}
        }
        dictA = {
            "cho": {},
            "Eaguru": {},
            "Ladleram": {},
            "Duvet": {},
            "kat": {},
            "Varun": {},
            "pmon": {},
            "leonid": {},
            "ggsnipes": {},
            "Prim": {},
            "Atsui": {},
            "Arta": {},
            "Thai": {},
            "Himsef": {},
            "Wineandbread": {},
            "V3NOMG": {},
            "Brandon": {}
        }
        dictB = {
            "10% Coupon": {},
            "Double Stuff Oreo": {},
            "Cast Iron Pan": {},
            "Killer Fork": {},
            "Thunder Kids": {}
        }
        dictC = {
            "An Old Boot": {},
            "A Torn Shirt": {},
            "A Ripped Glove": {},
            "A Tattered Scarf": {},
            "Ripped Jeans": {},
            "Paper Knife": {},
            "Literally Dogshit": {},
            "Stained Underwear": {}
        }

        convertList = []
        x=0
        while x < len(rollList):
            if rollList[x] < rarityTable["S"]:
                convertList.append(choice(list(dictS)))
                convertList[x] = "S: " + convertList[x]
            elif rollList[x] < rarityTable["A"]:
                convertList.append(choice(list(dictA)))
                convertList[x] = "A: " + convertList[x]
            elif rollList[x] < rarityTable["B"]:
                convertList.append(choice(list(dictB)))
                convertList[x] = "B: " + convertList[x]
            else:
                convertList.append(choice(list(dictC)))
                convertList[x] = "C: " + convertList[x]
            x+=1
        return convertList
        
    @commands.command()
    async def gacha(self, ctx, rollNumber : int = None):
        """
        Plays the gacha game.
        """
            
        #avoid overrolling
        if rollNumber is None:
            rollNumber = 10
        elif rollNumber > 10:
            await ctx.send("Please don't be greedy.")
            return
            
        rollList = []
        while len(rollList) < rollNumber:
            rollList.append(randint(1,10000))
        
        rolls = self._convertList(rollList)
        displayString = ""
        for i in rolls:
            displayString = displayString + i + "\n"
        await ctx.send("```" + displayString + "```")
        #change to embed form, when I learn how
    
    @commands.command()
    async def gachalist(self, ctx, listTier : str = None):
        """
        Shows the roll list with percentages. If a specific tier is specified, it will show only that tier instead.
        """
        
        #if listTier = None:
        await ctx.send("coming soon !!")