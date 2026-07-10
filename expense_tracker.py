expense_dict = {}
with open("expense.txt" , 'r') as file:
    for line in file:
        line = line.strip()
        if line and ":" in line:
            expense_name, expense_price = line.split(":", 1)
            expense_dict[expense_name.strip()] = int(expense_price.strip())
def expense_list():
    if not expense_dict :
        print("\nList is empty.")
        return
    print("\n|| CURRENT LIST ||")
    for expance_name, expense_price in expense_dict.items():
        print(f"- {expense_name}: {expense_price}")

def expense_add():
    name = input("Enter expense name: ").strip()
    price_input = int(input("Enter expense price: ").strip())

    for i in expense_dict:
        if name == i:
            price_input += expense_dict[name]
            expense_dict.update({name : price_input})
            print(f"'{name}' added successfully!")
        else:
            expense_dict[name] = price_input
            print(f"'{name}' added successfully!")    

print("|| EXPENCE TRACKER ||")
while True:
    choice = int(input("\n1.EXPENSE LIST\n2.ADD EXPENSE\n3.EXIT\n|| >>> ENTER THE OPERATION : "))
    if choice == 1:
        expense_list()
    if choice == 2:
        expense_add()
    if choice == 3:
        break
    else:
        print("Invalid Input!")

print("EXITING...")
with open("inventory.txt", "w") as file:
    for expense_name, expense_price in expense_dict.expense():
        file.write(f"{expense_name}:{expense_price}\n")
