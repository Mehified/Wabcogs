from .quest import Quest

async def setup(bot):
    bot.add_cog(Quest(bot))
