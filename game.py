# Rock, Paper, Scissors Assignment 
# by Helen Wang
# 2022 Summer NYU

# This is the "game.py" file
import random

print ("Rock, Paper, Scissors, Shoot!")
print ("------------------")
print ("Welcome 'Player One' to my Rock-Paper-Scissors game...") 
print ("------------------")

# Ask for Player One's input
YourChoice = input("Please make a selection ('rock', 'paper', or 'scissor'): ")## 
## print (f"You chose:'{YourChoice}'")

# Input validation

## valid_options = ["rock", "paper", "scissor"]
## UserChoice = YourChoice.lower()
## if UserChoice not in valid_options: 
##    print ("Invalid input. Please try again!")
##    exit ()
UserChoice = YourChoice.lower()

if UserChoice == "rock":
    P1 = 1
    print ("You chose: rock")
elif UserChoice == "paper":
    P1 = 2
    print ("You chose: paper")
elif UserChoice == "scissor":
    P1 = 3
    print ("You chose: scissor")
else: 
    print ("Invalid input. Please try again.")
    exit ()

# Function PC_Choice() to simulate computer choice
# Use the Random module

## PC_Choice = random.choice(valid_options)
## print ("Computer chose:", PC_Choice) 

x = random.random()
# print (round(x,2))

#def PC_Choice ():
if 0<x<=0.33:
    PC = 1
    print ("PC chose: rock")
elif 0.33<x<=0.67:
    PC = 2
    print ("PC chose: paper") 
elif 0.67<x<=1:
    PC = 3
    print ("PC chose: scissor")
# print (P1, PC)

# Function to determine the winner or tie

if (PC-P1)==1: 
    print ("Winner: computer")
elif(PC-P1)==0:
    print ("It is a tie!")
elif(PC-P1)==-2:
    print ("Winner: computer")
elif(P1-PC)==1: 
    print ("Great job! You won this game.") 
elif(P1-PC)==-2:
    print ("Great job! You won this game.")



