import random
from discord.ext import commands


class HeroQuest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        symbol_attack = ':crossed_swords:'
        symbol_shield = ':shield:'
        symbol_enemyshield = ':octagonal_sign:'
        self.die = [symbol_attack, symbol_attack, symbol_attack, symbol_shield, symbol_shield, symbol_enemyshield]

    @commands.command(name="hq")
    async def hqdice(self, ctx, number: int = 1):
        """Rolls dice for the game 'HeroQuest'"""
        rolls = []
        for i in range(0, number):
            roll = random.randint(0, 5)
            rolls.append(roll)
        msg = "HeroQuest: "
        rolls.sort()
        for i in rolls:
            msg += self.die[i]
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(HeroQuest(bot))
