print("|| HERE's THE VERY EASIEST QUIZ ||")

ans1 = int(input("What is 3*5 ? : "))
ans2 = int(input("What is 97+33 ?: "))
ans3 = int(input("What is 713+574 ? : "))
ans4 = int(input("what is 99*3 ? : "))
ans5 = int(input("What is 2+3 ? : "))

score = 0
if ans1 == 15:
    score += 1
if ans2 == 130:
    score += 1
if ans3 == 1287:
    score += 1
if ans4 == 297:
    score += 1
if ans5 == 5:
    score += 1

print(f"Your score is {score}")