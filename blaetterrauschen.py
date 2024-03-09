import asyncio
import random
from discord.ext import commands


class Blaetterrauschen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.die = ['1', '2', '2', '3', '3', '4']

    @commands.command(name="br")
    async def brdice(self, ctx):
        """Rolls dice for the game 'Blätterrauschen'"""
        async with ctx.typing():
            await asyncio.sleep(1)
            roll1 = random.randint(0, 5)
            roll2 = random.randint(0, 5)
            cloud = ""
            if roll1 == 2 or roll2 == 2:  # the die has a cloud on one of the 2s
                cloud += "+ :cloud:"
            msg = "Blätterrauschen:  :white_large_square: {} x {} :green_square: {}".format(self.die[roll1], self.die[roll2], cloud)
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(Blaetterrauschen(bot))
