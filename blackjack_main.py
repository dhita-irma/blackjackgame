from blackjack.blackjack_game import BlackJackGame
from blackjack.human_player import HumanPlayer

print("Welcome to the Black Jack game!\n")
player_chips = int(input("How much chips do you have?"))
player = HumanPlayer(player_chips)

while True:
    current_game = BlackJackGame(player)
    current_game.play_game()

    print(f"Your current chips are {player.money}")
    if not current_game.replay():
        print("Exit game.")
        break
