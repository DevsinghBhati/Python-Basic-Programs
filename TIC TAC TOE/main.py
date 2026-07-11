import numpy as np

matrix = np.array([[0,0,0],[0,0,0],[0,0,0]])

def print_board():
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

def check_wins():
    for i in range(3):
        if(matrix[i][0] == matrix[i][1] == matrix[i][2] == 1):
            print("USER 1 WINS")
            return True
        elif(matrix[i][0] == matrix[i][1] == matrix[i][2] == 2):
            print("USER 2 WINS")
            return True
        
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == 1:
            print("USER 1 WINS")
            return True
        elif matrix[0][i] == matrix[1][i] == matrix[2][i] == 2:
            print("USER 2 WINS")
            return True

    if(matrix[0][0] == matrix[1][1] == matrix[2][2] == 1 or matrix[2][0] == matrix[1][1] == matrix[0][2] == 1):
        print("USER 1 WINS")
        return True
    if(matrix[0][0] == matrix[1][1] == matrix[2][2] == 2 or matrix[2][0] == matrix[1][1] == matrix[0][2] == 2):
        print("USER 2 WINS")
        return True
        


print("|| TIC TAC TOE GAME ||")
print("Rules:\n1.TWO users\n2.EACH TERN ONE BY ONE\n")

print("Current board:")
print_board()

i = 0
while i < 9:
    game_over = False
    
    if i%2 == 0:
        print("\nUSER 1:")
        row = int(input("Enter Row (1-3): ")) - 1
        element = int(input("Enter Column (1-3): ")) - 1
        
        if matrix[row][element] == 0:
            matrix[row][element] = 1
            game_over = check_wins()
            print_board()
            i += 1
        else:
            print("Spot already taken! Try again.")

    else:
        print("\nUSER 2:")
        row2 = int(input("Enter Row (1-3): ")) - 1
        element2 = int(input("Enter Column (1-3): ")) - 1
        
        if matrix[row2][element2] == 0:
            matrix[row2][element2] = 2
            game_over = check_wins()

            print_board()
            i += 1
        else:
            print("Spot already taken! Try again.")
            
    if game_over:
        break

    if i == 9 and not game_over:
        print("Draw")