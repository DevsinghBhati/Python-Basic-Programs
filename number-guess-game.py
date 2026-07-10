import random   

print("|| NUMBER GUESS GAME ||")

def game(max_limit):
    random_int = random.randint(1,max_limit)
    print("I am selecting...")
    print("\nYEAH, i have selected")
    print(f"Guess my number in the range from 1 to {max_limit}")
    count = 0
    for i in range(5):
        user_guess = int(input("guess my number : "))
        if user_guess == random_int:
            print("YOU WON , YOU GOT IT")
            break
        elif user_guess > random_int:
            print("guess lower")
        else:
            print("guess higher")
        count += 1
        print(f"You have {5-count} attemps now !")


while True:
    choice = int(input("1.EASY\n2.MEDIUM\n3.HARD\n4.EXIT\nEnter Level : "))
    if choice == 1:
        game(50)
    if choice == 2:
        game(100)
    if choice == 3:
        game(200)
    if choice == 4:
        break
    else:
        print("INVALID INPUT!")
print("Exiting...")