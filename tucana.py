import asyncio
from discord.ext import commands
from tucanacard import TucanaDeck, TucanaCard


class Tucana(commands.Cog):
    def __init__(self, bot):
        self.deck = TucanaDeck()

    @commands.command(name="tuc")
    async def tucdraw(self, ctx):
        """Draws cards for the game 'Trails of Tucana'."""
        message = ">>> "
        async with ctx.typing():
            await asyncio.sleep(0.7)
            card1, card2, shuffled = self.deck.draw_cards()
            if shuffled:
                # nur ausgeben, dass Wertung, dann nochmal neu mischen
                message += "Stapel aufgebraucht!\nBitte (Teil-) Wertung durchführen."
                self.deck.initialize_deck()
            else:
                message += str(len(self.deck.cards_to_draw)) + " verbleibende Karten.\n"
                message += self.create_message_for_cards(card1, card2)
        await ctx.send(message)

    @commands.command(name="tuc-reset")
    async def tucreset(self, ctx):
        """Resets the deck for 'Trails of Tucana'."""
        async with ctx.typing():
            await asyncio.sleep(0.5)
            self.deck.initialize_deck()
        await ctx.send("Deck zurückgesetzt.")

    def create_message_for_cards(self, card1, card2):
        text_for_cards = {
            TucanaCard.DESERT: ":desert: Wüste",
            TucanaCard.JOKER: ":black_joker: Joker",
            TucanaCard.MOUNTAIN: ":mount_fuji: Gebirge",
            TucanaCard.WATER: ":ocean: Wasser",
            TucanaCard.WOODS: ":palm_tree: Wald"
        }
        message = "gezogene Karten: \n" + text_for_cards[card1] + ", \n" + text_for_cards[card2]
        return message


def setup(bot):
    bot.add_cog(Tucana(bot))
