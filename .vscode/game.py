
import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3

playagain = True
while playagain :
    
    print('')
    playerchoise = input("Enter.... \n1  for Rock , \n2 for Paper ,\n3 for Scissors:\n\n")

    print(playerchoise)

    player = int(playerchoise)

    computerchoise = random.choice('123')

    computer = int(computerchoise)

    print("")
    print("You chose " + str(RPS(player)).replace("RPS." , "")+ ".")
    print("Python chose " + str(RPS(computer)).replace("RPS." , "") + ".") 
    print("")

    if player == 1 and computer == 3:
        print("You Win")
    elif player ==2 and computer ==1 :
        print("You Win")
    elif player == 3 and computer == 2:
        print("You win")
    elif player == computer : 
        print("Game Tie !!")
    else:
        print("Pyton win!")
        if player >3 or player <1 :
             print("Enter Number between 1 to 3")
        
    playagain = input('\n Play Again ? \n Y for yes \n N for no \n\n')
    if playagain.lower() == 'y':
        continue
    else : 
        print("Thank You for playing ")
        playagain = False   
  
    sys.exit("bye")
