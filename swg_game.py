# This is snake water gun game

import random
comp_lst = ['s', 'w', 'g']
tie = 0
win = 0
loss =0
print("Let's play Snake Water Gun game with AI")
print("Rules")
print("Snake will drink water")
print("gun can kill snake")
print("water can damage gun")
print("What You will select  ")


for i in range(0, 10):
    comp_choice = random.choice(comp_lst)
    # print(comp_choice)
    print("Write 's' for 'snake', 'w' for 'water' , 'g' for gun")
    user_choice = input()
    if comp_choice == user_choice :
        print("Its a Tie")
        tie +=1
    if comp_choice== 's':
        if user_choice =='g':
            win+=1
        elif user_choice=='w':
            loss+= 1
    elif comp_choice=='g':
        if user_choice=='w':
            win+= 1
        elif user_choice=='s':
            loss+=1
    elif comp_choice=='w':
        if user_choice=='s':
            win+=1
        elif user_choice=='g':
            loss+= 1
    else:
        print("You had given the wrong input")
    print("Your score is ")
    print(f"Tie score:-{tie}")
    print(f"Win score :- {win}")
    print(f"Loss score: {loss}")
if win>loss:
    print("You Won the game")
elif loss>win:
    print("You lost the game")
else:
    print("It's tie")


