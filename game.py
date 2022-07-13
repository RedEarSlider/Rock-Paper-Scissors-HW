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
print (f"You chose:'{YourChoice}'")

# Input validation

valid_options = ["rock", "paper", "scissor"]
UserChoice = YourChoice.lower()
if UserChoice not in valid_options: 
   print ("Invalid input! Please try again.")
   exit ()

if UserChoice == "rock":
    P1 = 1
elif UserChoice == "paper":
    P1 = 2
elif UserChoice == "scissor":
    P1 = 3

# PC_Choice() to simulate computer choice
# Use the Random module

PC_Choice = random.choice(valid_options)
print ("Computer chose:", PC_Choice) 

if PC_Choice == "rock":
    PC = 1
elif PC_Choice == "paper":
    PC = 2
elif PC_Choice == "scissor":
    PC = 3

# To determine and display the result: winner or tie

if (PC-P1)==1 or (PC-P1)==-2: 
    print ("Winner: computer")
elif(PC-P1)==0:
    print ("It is a tie!")
elif(P1-PC)==1 or (P1-PC)==-2: 
    print ("Great job! You won this game.") 



