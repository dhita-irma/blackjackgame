from .deck import Deck
from .comp_dealer import CompDealer


class BlackJackGame:

    def __init__(self, player1):
        self.player1 = player1
        self.dealer = CompDealer()
        self.player1.current_score = 0  # setting human player's score to zero
        self.bet_amount = 0

        self.deck = Deck()
        self.deck.shuffle()

    def deal_card(self, player, num_draw):
        """Deal certain number of cards to a player."""
        for i in range(num_draw):
            card_drawn = self.deck.draw_card()
            player.add_card(card_drawn)

    def player_turn(self, currentplayer):
        """Lets the player take hit and returns their state: BUSTED, WIN, or PASS"""
        while True:
            print(f"Current player's score is: {currentplayer.current_score}")
            if currentplayer.take_hit():            # ask if player wants to take a hit
                self.deal_card(currentplayer, 1)    # deal a player a card
                if currentplayer.bust_check():      # check if the player bust
                    return "busted"
                if currentplayer.win_check():       # check if the player wins
                    return "win"
            else:
                return "pass"

    def player_win(self):
        print("Congratulation, you win!")
        self.player1.update_money(self.bet_amount)

    def player_lose(self):
        print("You lose!")
        self.player1.update_money(self.bet_amount * (-1))

    def play_game(self):
        self.bet_amount = self.player1.bet()

        self.deal_card(self.player1, 2)
        self.deal_card(self.dealer, 2)

        # HUMAN PLAYER'S TURN
        print(f"This is your turn.")
        human_outcome = self.player_turn(self.player1)
        if human_outcome == "win":
            self.player_win()
        elif human_outcome == "busted":
            print("You busted.")
            self.player_lose()
        else:
            print("This the dealer's turn.")
            dealer_outcome = self.player_turn(self.dealer)
            if dealer_outcome == "busted":
                print("The dealer busted.")
                self.player_win()
            elif dealer_outcome == "win":
                print("Dealer wins!")
                self.player_lose()
            elif self.player1.current_score > self.dealer.current_score:
                print("You score is greater than the dealer's.")
                self.player_win()
            elif self.player1.current_score < self.dealer.current_score:
                print("You score is less than the dealer's.")
                self.player_lose()
            else:
                print("It is a tie!")

    def replay(self):
        """Determine if the users want to play game again.
        Returns boolean True if they do."""
        play_again = input('Do you want to play again? (Y/N):').upper()
        while play_again != 'Y' and play_again != 'N':
            play_again = input("Please enter 'Y' or 'N': ")
        return play_again == 'Y'