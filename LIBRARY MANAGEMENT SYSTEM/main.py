import datetime
import json

x = datetime.datetime.now()
print(x.strftime("Today's Date: %x\n"))

with open("books.json", "r") as file:
    books = json.load(file)

def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def view_books():
    if not books:
        print("\nNo books available in the library right now.")
        return
    print("\n|| AVAILABLE BOOKS ||")
    count = 1
    for book, info in books.items():
        if info["status"] == "Available":
            print(f"{count}: {book} (Available)")
        else:
            print(f"{count}: {book} (Issued on {info['issue_date']})")
        count += 1
    print("\n")

def issue_book():
    book_name = input("Enter the book name: ").strip().upper()
    if book_name in books:
        if books[book_name]["status"] == "Issued":
            print(f"{book_name} is already issued.\n")
            return
        
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        books[book_name]["status"] = "Issued"
        books[book_name].update({"issue_date" : f"{today}"})
        save_books()
        print(f"'{book_name}' book issued successfully on {today}.\n")
    else:
        print(f"'{book_name}' book is not available.\n")

def return_book():
    book_name = input("Enter the book name to return: ").strip().upper()
    if book_name in books:
        if books[book_name]["status"] == "Available":
            print(f"The library already has '{book_name}'.\n")
            return
        issue_date_str = books[book_name]["issue_date"]
        issue_date = datetime.datetime.strptime(issue_date_str, "%Y-%m-%d")
        return_date = datetime.datetime.now()
        
        days_diff = (return_date - issue_date).days
        penalty = 100000
        if days_diff > 60 :
            print("You need to pay penalty : ")
            print(f"Penalty amount is : {penalty} $")
        else:
            print("Returned on time")
        books[book_name]["status"] = "Available"
        [books][book_name].update({"issue_date" : None})
        save_books()
        print(f"'{book_name}' returned successfully\n")
    else:
        print(f"'{book_name}' book is not in library records.\n")


print("|| Welcome to THE LIBRARY ||\n")
while True:
    try:
        print("1. Display Books\n2. Issue Book\n3. Return Book\n4. Exit")
        choice = int(input("Enter the operation: "))
        
        if choice == 1:
            view_books()
        elif choice == 2:
            issue_book()
        elif choice == 3:
            return_book()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid Input! Please choose between 1 to 4.\n")
    except ValueError:
        print("Please enter a valid number.\n")
