import random
charlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

random_char = random.choice(charlist)

i = 0


print("WELCOME TO HANGMAN!")
while  i < 5:
    guess = ("guess the number: ").strip().upper()

    rand = charlist.index(random_char)
    gue = charlist.index(guess)

    if(rand == gue):
        print("You won!, YOU GOT IT!")
        break
    if(rand < gue):
        print("lower")
    if(rand > gue):
        print("higher")
    i+=1