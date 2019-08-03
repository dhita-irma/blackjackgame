from .player import Player


class CompDealer(Player):

    def __init__(self):
        super().__init__()

    def take_hit(self):
        """Returns a boolean value True if player wants to take a hit."""
        return self.current_score < 18
