books = [ 'PYTHON', 'C' , 'JAVA','C++']

def view_books():
    count = 1
    print("|| AVAILABLE BOOKS ||")
    for book  in books:
        print(count,end=":")
        print(book)
        count += 1

def issue_book():
    book_name = input("Enter the book name :")
    if book_name in books :
        books.remove(book_name)
        print(f"{book_name} book issues successfully.")
    else:
        print(f" {book_name} Book not available")

def return_book():
    book_name = input("Enter the book name :")
    books.append(book_name)
    print("book returned successfully.")

print("|| Welcome to THE LIBRARY ||\n")
while True:
    choice = int(input("1. Display Books\n2. Issue Book\n3. Return Book\n4. Exit\nEnter the operation : "))
    if choice == 1:
        view_books()
    if choice == 2:
        issue_book()
    if choice == 3:
        return_book()
    if choice == 4:
        break
    else:
        print("Invalid Input !")
    
print("Exiting...")