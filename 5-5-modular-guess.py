from funkcije_za_igru import play_game
from funkcije_za_igru import top_scores

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        top_scores()
    else:
        break
