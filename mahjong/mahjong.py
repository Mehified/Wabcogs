from random import randint
from redbot.core import commands
from redbot.core import Config
import discord

class Mahjong(commands.Cog):
    """
    Plays mahjong.
    """
    def __init__(self, bot):
        self.bot = bot
        self.gameStarted = False
        self.tilesWall = []
        self.tilesHand = []
        self.tilesDeadwall = []
        self.tilesDora = []
        self.tilesDiscard = []
    
    def setBoard(self):
        #define all tiles, initially in wall. move to init?
        self.tilesWall = [
        "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
        "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
        "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
        "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
        "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
        "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
        "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
        "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
        "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
        "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
        "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
        "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
        "E","E","E","E","S","S","S","S",
        "W","W","W","W","N","N","N","N",
        "RD","RD","RD","RD","GD","GD","GD","GD",
        "WD","WD","WD","WD"]
        self.tilesHand = []
        self.tilesDeadwall = []
        self.tilesDora = []
        self.tilesDiscard = []
    
    #add function for tile to picture/embed?
    
    def getHand(self):
        self.tilesHand = [""]*13
        tilesTotal = len(self.tilesWall)
        for i in range(len(self.tilesHand)):
            self.tilesHand[i] = self.tilesWall[randint(0,tilesTotal)]
    
    @commands.command()
    async def mahjong(self, ctx, cmd : str = "start"):
        """
        Main function for starting / stopping a mahjong game.
        """
        
        #check if game is already running or not
        if cmd == "start":
            self.gameStarted = True
            await ctx.send("Starting a game.")
            self.setBoard()
            #makedeadwall
            #pickdora
            self.getHand()
            await ctx.send("```" + str(self.tilesHand) + "```") #shift display to embed
            #initialize wall/hand/etc.
        elif cmd == "stop":
            self.gameStarted = False
            await ctx.send("Stopping.")
            #reset conditions? or just allow init to handle?
        elif cmd == "restart":
            #reinitializes hand/wall/etc.
            await ctx.send("not in yet")
        else:
            await ctx.send("Not a valid command. See help for more.")
        
        #await ctx.send("done")
    
    @commands.command()
    async def discard(self, ctx, tileDiscard : str = None):
        """
        Discards a tile of choice from your hand
        """
        #move to separate function? has to be async to message though
        if self.gameStarted == True:
            pass
        else:
            await ctx.send("Game must be started. Please use [p]mahjong to start a game.")
            return
            
        #getHandTiles()
        
        if tileDiscard == None:
            await ctx.send("No tile selected. Please choose a valid tile from your hand.")
        elif tileDiscard in self.tilesHand:
            self.tilesDiscard.append(tileDiscard)
            self.tilesHand.remove(tileDiscard)
            
            tilesTotal = len(self.tilesWall)
            if tilesTotal > 0:
                self.tilesHand.append(self.tilesWall[randint(0,tilesTotal)])
            else:
                await ctx.send("Exhaustive draw.")
                #check hand status
            await ctx.send("```" + str(self.tilesHand) + "```")
        else:
            await ctx.send("That's not in your hand.")
            
    @commands.command()
    async def tile(self, ctx, tile: str = None):
        """
        Displays a random tile, (embed format soontm)
        """
        self.setBoard()
        tilesTotal = len(self.tilesWall)
        await ctx.send("```"+self.tilesWall[randint(0,tilesTotal)]+"```")
        
    @commands.command()
    async def show(self, ctx, cmd: str = None):
        """
        See a particular area of the board.
        """
        
        if cmd == "hand":
            await ctx.send("```" + str(self.tilesHand) + "```")
        elif cmd == "wall":
            await ctx.send("There are {} tiles left".format(len(self.tilesWall)))
        elif cmd == "discard":
            await ctx.send("```" + str(self.tilesDiscard) + "```")
        #add more show
        else:
            await ctx.send("?")
