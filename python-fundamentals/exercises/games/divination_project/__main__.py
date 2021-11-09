from exercises.games.divination_project.divination import Divination
from random import randint

mode = input("Choose a game mode\n1. Easy\n2. Intermediate\n3. Hard\n-> ")
if mode != "1" and mode != "2" and mode != "3":
    print("Unrecognized mode")
    exit(0)
game = Divination(randint(0, 100), int(mode))
game.start()

