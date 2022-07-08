# Rock, Paper, Scissors Assignment 
# by Helen Wang
# 2022 Summer NYU

# This is the "game.py" file
from random import random


print ("Rock, Paper, Scissors, Shoot!")
print ("------------------")
print ("Welcome 'Player One' to my Rock-Paper-Scissors game...") 
print ("------------------")

# Ask for Player One's input
YourChoice = input("Please choose either 'rock', 'paper', or 'scissor': ")

# Input validation
if YourChoice == "rock":
    print ("Your chose: rock")
elif YourChoice == "paper":
    print ("Your chose: paper")
elif YourChoice == "scissor":
    print ("Your chose: scissor")
else: print ("Invalid input. Please try again.")
exit ()

# Function PC_Choice() to simulate computer choice
# Use the Random module
def PC_Choice ():
 x = random
 print (type(x))
 print (x)
end ()


