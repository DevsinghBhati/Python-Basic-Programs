import random

mylist = ["rock", "paper", "scissor"]




while  True:
    x =random.choice(mylist)    
    choice = int(input("1.ROCK\n2.PAPER\n3.SCISSOR\n4.EXIT \nEnter your choice: "))
    if choice == 1:
        if x == "rock" :
            print("same, continue")
        elif x ==  "paper":
            print("You won...")
        else:
            print("Computer wins")
    if choice == 2:
        if x == "rock" :
            print("You won...")
        elif x ==  "paper":
            print("same, continue")
        else:
            print("Computer wins")
    if choice == 3:
        if x == "rock" :
            print("Computer wins")
        elif x ==  "paper":
            print("You won...")
        else:
            print("same, continue")
    if choice == 4:
        break