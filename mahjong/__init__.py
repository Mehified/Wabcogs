from .mahjong import Mahjong

def setup(bot):
    bot.add_cog(Mahjong(bot))
