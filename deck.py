from .card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    """Deck is composed of cards."""
    def __init__(self):
        self.deck = []  # a list of card object
        for suit in ['Heart', 'Diamond', 'Spade', 'Club']:
            for i in range(2, 10):
                card = Card(suit, str(i))
                self.deck.append(card)
            for i in ['Ace', 'King', 'Queen', 'Jack']:
                card = Card(suit, i)
                self.deck.append(card)

    def shuffle(self):
        """Change the state of the deck object to a be random."""
        random.shuffle(self.deck)

    def draw_card(self):
        """Pop out the last card in the deck.
        Returns a card object."""
        return None if len(self.deck) == 0 else self.deck.pop()
