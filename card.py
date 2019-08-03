class Card:

    def __init__(self, suit, rank):
        """
        :param suit: string, one of Heart, Diamond, Spade, or Club.
        :param rank: string, 2 - 9, Jack, Queen, King, or Ace.
        """
        self.rank = rank
        self.suit = suit

    def value(self, current_score):
        """Determine card value based on card type.
        Returns integer."""
        if '1' <= self.rank <= '9':
            return int(self.rank)
        elif self.rank == 'King' or self.rank == 'Queen' or \
                self.rank == 'Jack':
            return 10
        elif self.rank == 'Ace':
            if current_score <= 10:
                return 11
            return 1
