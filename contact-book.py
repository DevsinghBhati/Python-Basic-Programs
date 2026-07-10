import json
with open("contact-book.json", "r") as file:
    data = json.load(file)


def add_contact(name, contact):
    if name in data or contact in data.values():
        print("Contact Name or Number already exists!")
    else:
        data[name] = contact
        print(f"Contact {name} added successfully.")

def delete_contact(contact):
    key_to_delete = None
    for name, number in data.items():
        if number == contact:
            key_to_delete = name
            break
    
    if key_to_delete:
        data.pop(key_to_delete)
        print("Contact deleted successfully.")
    else:
        print("Contact number not found.")

while True:
    print("\n1. ADD contact\n2. View contacts\n3. Delete contacts\n4. EXIT")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        while True:
            name = input("Enter the name of person: ")
            try:
                contact = int(input(f"Enter the PHONE NUMBER of {name}: "))
                add_contact(name, contact)
            except ValueError:
                print("Invalid phone number format. Use numbers only.")
            
            ask = input("\nWant to add more contacts? (y/n): ").lower()
            if ask == 'n':
                break
                
    elif choice == 2:
        print("\n|| ALL CONTACTS ||")
        if not data:
            print("No contacts found.")
        for name, number in data.items():
            print(f"{name} : {number}")
            
    elif choice == 3:
        contact = int(input("Enter the PHONE NUMBER to delete: "))
        delete_contact(contact)
            
    elif choice == 4:
        print("\nExiting...")
        break
    else:
        print("Invalid choice. Please select 1-4.")

with open("contact-book.json", "w") as file:
    json.dump(data, file, indent=4)