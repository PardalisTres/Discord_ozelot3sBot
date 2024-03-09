from enum import Enum
from derange import derange


class TucanaCard(Enum):
    DESERT = 0
    JOKER = 1
    MOUNTAIN = 2
    WATER = 3
    WOODS = 4


class TucanaDeck:
    cards_to_draw = []
    # cards_drawn = []

    def initialize_deck(self, desert: int = 8, joker: int = 2, mountain: int = 6, water: int = 4, woods: int = 7):
        """Initializes this TucanaDeck with the given number of cards of each type."""
        self.cards_to_draw.clear()
        for i in range(desert):
            self.cards_to_draw.append(TucanaCard.DESERT)
        for i in range(joker):
            self.cards_to_draw.append(TucanaCard.JOKER)
        for i in range(mountain):
            self.cards_to_draw.append(TucanaCard.MOUNTAIN)
        for i in range(water):
            self.cards_to_draw.append(TucanaCard.WATER)
        for i in range(woods):
            self.cards_to_draw.append(TucanaCard.WOODS)
        derange(self.cards_to_draw)

    def draw_cards(self):
        """Draws the next two cards for a new move in the game."""
        deck_shuffled = False
        if len(self.cards_to_draw) < 2:
            self.initialize_deck()
            deck_shuffled = True
        return self.cards_to_draw.pop(), self.cards_to_draw.pop(), deck_shuffled
