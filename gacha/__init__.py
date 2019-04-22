from .gacha import Gacha

def setup(bot):
    bot.add_cog(Gacha(bot))
