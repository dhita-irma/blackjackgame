class Player:

    def __init__(self):
        self.current_score = 0

    def add_card(self, card):
        self.current_score += card.value(self.current_score)

    def bust_check(self):
        """Returns True if the player is busted."""
        return self.current_score > 21

    def win_check(self):
        """Returns True if the player has 21."""
        return self.current_score == 21
