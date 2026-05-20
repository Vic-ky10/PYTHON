import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_rps():

    while True:

        print("")
        playerchoice = input(
            "Enter.... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n"
        )

        if playerchoice not in ['1', '2', '3']:
            print("You must enter 1, 2, or 3.")
            continue

        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print("")
        print(f"You chose  { str(RPS(player)).replace("RPS.", "") } .")
        print(f"Python chose { str(RPS(computer)).replace("RPS.", "") }.")
        print("")

        # Winning conditions
        if player == 1 and computer == 3:
            print("You Win!")
        elif player == 2 and computer == 1:
            print("You Win!")
        elif player == 3 and computer == 2:
            print("You Win!")
        elif player == computer:
            print("Game Tie!!")
        else:
            print("Python Wins!")

        # Play again
        while True:
            playagain = input("\nPlay again?\nY for Yes\nQ for Quit\n").lower()

            if playagain in ['y', 'q']:
                break
            else:
                print("Enter Y or Q only.")

        if playagain == 'y':
            continue
        else:
            print("Thank You for playing!")
            sys.exit()


play_rps()