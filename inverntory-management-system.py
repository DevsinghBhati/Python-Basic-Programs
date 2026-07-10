
inventory = {}
with open("inventory.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line and ":" in line:
            item, stock = line.split(":", 1)
            inventory[item.strip()] = int(stock.strip())

def add_items():
    item = input("\nEnter item name: ").strip()
    
    if item in inventory:
        print(f"Already have this item (Current stock: {inventory[item]})")
        print("|| Let's update the stock ||")
        # Add new stock to existing stock
        new_stock = int(input("Enter stock to add: "))
        inventory[item] += new_stock
    else:
        stock = int(input("Enter stock: "))
        inventory[item] = stock
    print(f"Success: {item} stock is now {inventory[item]}")

def view_list():
    if not inventory:
        print("\nInventory is empty.")
        return
    print("\n|| CURRENT INVENTORY ||")
    for item, stock in inventory.items():
        print(f"- {item}: {stock}")

print("|| INVENTORY ||")
while True:
    choice = int(input("\n1.ADD ITEMS\n2.VIEW LIST\n3.EXIT\nChoose an option: "))
    if choice == 1:
        add_items()
    elif choice == 2:
        view_list()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

print("EXITING...")
with open("inventory.txt", "w") as file:
    for item, stock in inventory.items():
        file.write(f"{item}:{stock}\n")
