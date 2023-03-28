# Write a console program that implements a simple 1-player dice game called "Piglet" (based on the game "Pig"). The player's goal is to accumulate as many points as possible without rolling a 1. Each turn, the player rolls the die if they roll a 1, the game ends and they get a score of 0. Otherwise, they add this number to their running total score. The player then chooses whether to roll again, or end the game with their current pototal. Here is an example dialogue where the user plays until rolling a 1, which ends the game with 0 points:
# 
# Welcome to Piglet!
# You rolled a 5
# Roll again? yes
# You rolled a 4
# Roll again? yes
# You rolled a 1
# You got 0 points.
# 
# Here is another example dialogue where the user stops early and gets to end the game with 10 points:
# 
# Welcome to Piglet!
# You rolled a 6
# Roll again? y
# You rolled a 2
# Roll again? y
# You rolled a 2
# Roll again? n
# You got 10 points.
# 
# Write code below
import random
print("Welcome to Piglet!")
roll = random.randint(1, 6)
print("You rolled a " + str(roll))
if roll == 1:
    print("You got 0 points.")
else:
    total = roll
    roll_again = input("Roll again? ")
    while roll_again == "y" or roll_again == "yes":
        roll = random.randint(1, 6)
        print("You rolled a " + str(roll))
        if roll == 1:
            print("You got 0 points.")
            break
        else:
            total += roll
            roll_again = input("Roll again? ")
    if roll_again == "n" or roll_again == "no":
        print("You got " + str(total) + " points.")
