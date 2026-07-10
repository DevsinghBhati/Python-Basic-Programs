total_seats = {
    'A' : ['[]','[]','[]','[]','[]'],
    'B' : ['[]','[]','[]','[]','[]'],
    'C' : ['[]','[]','[]','[]','[]'],
    'D' : ['[]','[]','[]','[]','[]'],
    'E' : ['[]','[]','[]','[]','[]']
}

def view_seats():
    print(type(total_seats))
    print("  1 2 3 4 5")
    for i in (total_seats):
        print(i,end=':')
        for j in total_seats[i] :
            print(j, end='')
        print("\n")

def seats_occupy():
    view_seats()
    seat_number = int(input("Enter how much seats :"))
    for _ in range(seat_number):
        row = input("Enter which ROW (A-E): ").upper()
        number = int(input("Enter seat number (1-5): "))
        index = number - 1
        
        if row in total_seats:
            if 0 <= index < len(total_seats[row]):
                if total_seats[row][index] == '[]':
                    total_seats[row][index] = '*' 
                    print(f"Seat {row}{number} booked successfully!")
                else:
                    print(f"Seat {row}{number} is already occupied.")
            else:
                print("Invalid seat number. Please choose between 1 and 5.")
        else:
            print("Invalid row. Please choose between A and E.")
    
    view_seats()


print("|| WELCOME TO HOLLYWOOD CINEMA ||")
seats_occupy()
