# Rock, Paper, Scissors Assignment 
# by Helen Wang
# 2022 Summer NYU

# This is the "game.py" file
from random import random
from re import X


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


# Function PC_Choice() to simulate computer choice
# Use the Random module
import random
x = random.random()
print (round(x,2))

#def PC_Choice ():
if 0<x<0.33:
    print ("PC chose: rock")
elif 0.33<x<0.67:
    print ("PC chose: paper") 
elif 0.67<x<1:
    print ("PC chose: scissor")

# Function to determine the winner or tie




