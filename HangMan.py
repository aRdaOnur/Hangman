import random 
import os 

print("Let's Play HangMan")
print("Game Rules: You have 1 more life than the length of the hidden word, if you run out of lives => the game is over,\n you will try to guess the word. So let's start")
secretWords = ["mamur","mamur","mamur"]
screenWords = ""

live = len(secretWords)+1 
x = random.randint(0, len(secretWords)-1)
trueWords = ""

while live>0 and len(set(trueWords)) != len(set(secretWords[x])):
    
    while True:
        guess = input("Enter Your GUESS (only 1 letter): ")
        
        if len(guess) != 1 :
            print("Only 1 letter!!")
        elif not guess.isalpha():
            print("Input only string!")
        else:
            if guess in set(trueWords):
                print("Word already exists")
                continue
            break

    
    for i in secretWords[x]:
        if i == guess:
            screenWords += i 
            
        if i in screenWords:
            print(i, end=" ")

        else:
            print("*", end=" ")


    if guess not in secretWords[x]:
        live -=1
        print("Wrong!")
        if live == 0:
            print("You Lose")


    if guess in secretWords[x]:
        print("True!")
        trueWords += guess


    if len(set(trueWords)) == len(set(secretWords[x])):
        print("YOU WON!!!")
        break
        

        
