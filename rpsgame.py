#Introduction
import time
import random
print("Hello")
time.sleep(1)
print("Welcome to Rock, ", end= ' ') ,
time.sleep(0.3)
print("Paper, ", end= ' ') ,
time.sleep(0.3)
print("Scissor", end= ' ') ,
time.sleep(0.7)
print("...")
time.sleep(1)
print("Dear Player, The fate of the world lies on your hands..");
time.sleep(1.8)
print("May I know you name? ")
player_name= input()
print(f"{player_name} , sounds like the name of a hero")
time.sleep(1)
print("My time is almost up ... ")
time.sleep(0.7)
print(" Do you know how to use the sacred technique of...")
time.sleep(0.3)
b =input("Rock, Paper, Scissor (y or n) ?").upper()
if b=="Y":
    print("Good.. Proceed and save the world!")
elif b=="N" :
    print("These are the sacred rules, Rock beats Paper, Paper beats Rock and Scissor beats paper")
    print(" Go ahead and save the world!")
 


#Global Declares
x = int
y = 10
#Random Logic
computerRange = ["rock", "paper", "scissors"]
computer = random.choice(computerRange)

#User Input
user = input("Enter a choice (rock, paper, scissors): ")
print(f"\nYou chose {user}, antagonist chose {computer}.\n")
time.sleep(1)

#Winning Logic
x = int
if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
        
    else:
        print("Paper covers rock! You lose.")
        print ("The End")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
        
    else:
        print("Scissors cuts paper! You lose.")
        print ("The End")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")

    else:
        print("Rock smashes scissors! You lose.")
        print ("The End")