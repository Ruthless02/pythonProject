#This is my first Python program
import random
random.randint(1,3)
player=int(input("Enter a number (between 1-3): "))
rock=1
paper=2
scissor=3
computer=random.randint(1,3)
if player==1: #and computer==3:
    print("Computer wins")
elif player==3: #and computer==2:
    print("Player wins")
elif player==1: #and computer==2:
    print("Computer wins")
elif player==3: #and computer==1:
    print("Player wins")
elif player==2: # and computer==3:
    print("Computer wins")
elif player==2: #and computer==1:
    print("Player wins")
else:
    print("Invalid input")
