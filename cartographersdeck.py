from enum import Enum
from derange import derange


class CartographersCardType(Enum):
    LAND = 0
    MONSTER = 1
    RUINS = 2


class CartographersCard:
    """Eine Karte im Spiel '"'Der Kartograph'."""

    def __init__(self, cardname, cardtype: CartographersCardType, cardtext, cardvalue: int = 0):
        self.cardname = cardname
        self.cardtype = cardtype
        self.cardtext = cardtext
        self.cardvalue = cardvalue


class CartographersDeck:
    """Ein Deck im Spiel 'Der Kartograph'."""

    game_deck = []

    def __init__(self):
        self.create_game_deck()

    def create_game_deck(self):
        self.game_deck.clear()
        self.game_deck.append(CartographersCard("Baumwipfeldorf", CartographersCardType.LAND, "Wald oder Dorf\n`  XX`\nXXX``", 2))
