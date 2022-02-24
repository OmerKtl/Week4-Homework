"""
Number Guessing Game
General Information:
I want to play a game which I can guess a number. 
The computer chooses a number in the range I chose. 
So that I can try to find the correct number which was selected by computer.
Acceptance Criteria:
* Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. 
* Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low. 
* If the user guesses correctly, the program should print total time and total number of guesses. 
* You must import some required modules or packages You can assume that the user will enter valid input
"""
import random
import time
start_number=int(input("Please Enter The Starting Number :"))
finish_number=int(input("Please Enter The Finishing Number:"))
num_list=[]
for i in range(start_number,finish_number+1):
    num_list.append(i)
n=int(random.sample(num_list,1)[0])
syc=0
guess_number=int(input("Guess What is The Random Number:"))
if guess_number:
    strt=time.time()
    syc+=1
while True:
    if guess_number==n:
        fnt=time.time()
        print("\nYes!!!! You found the number in {} seconds with {} number of guess...\n".format(round((fnt-strt),2),(syc)))
        break
    elif guess_number>n:
        print("Too high!!")
        guess_number=int(input("Guess What is The Random Number:"))
        syc+=1
    elif guess_number<n:
        print("Too low!!")
        guess_number=int(input("Guess What is The Random Number:"))
        syc+=1