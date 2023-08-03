import random 

print("Let's Play HangMan")
print("Game Rules: You have 1 more life than the length of the hidden word, if you run out of lives => the game is over, you will try to guess the word. So let's start")
secretWords = ["apple","banana","orange"]
screenWords = ""

live = len(secretWords)+1
x = random.randint(0, len(secretWords)-1)
trueWords = ""

while live>0 and len(trueWords) != len(secretWords[x]):
    
    while True:
        guess = input("Enter Your GUESS (only 1 word): ")
        
        if len(guess) != 1 :
            print("Only 1 word!!")
        elif not guess.isalpha():
            print("Input only word!")
        else:
            break
    
    for i in secretWords[x]:
        if i == guess:
            screenWords += i 
            
        if i in screenWords:
            print(i)
        else:
            print("*")

    if guess not in secretWords[x]:
        live -=1
        print("Wrong!")
        if live == 0:
            print("You Lose")

    if guess in secretWords[x]:
        print("True!")
        trueWords += guess

    if len(trueWords) == len(secretWords[x]):
        print("YOU WON!!!")
        break
        

        
