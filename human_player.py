from .player import Player


class HumanPlayer(Player):

    def __init__(self, money):
        super().__init__()
        self.money = money

    def take_hit(self):
        """Returns a boolean value True if player wants to take a hit."""
        while True:
            hit = input("Do you want to take a hit (Y/N): ").upper()
            if hit == 'Y':
                return True
            if hit == 'N':
                return False

    def bet(self):
        """Take a bet as user input and returns an integer."""
        while True:
            bet_amount = input("How much do you want to bet? ")
            try:
                bet_amount = int(bet_amount)
                if bet_amount <= self.money:
                    return bet_amount
                print("You don't have enough money")
            except ValueError:
                print("Input is not an integer.")

    def update_money(self, winnings):
        self.money += winnings
