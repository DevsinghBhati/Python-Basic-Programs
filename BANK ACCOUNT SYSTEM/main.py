


account = {
    "Account Number": 123456,
    "PIN": 1234,
    "Name": "Dev",
    "Balance": 0,
    "History": []
}

def deposit():
    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid Amount!")
        return

    account["Balance"] += amount
    account["History"].append(f"Deposited  {amount}")

    print(f" {amount} Deposited Successfully.")


def withdraw():
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid Amount!")
        return

    if amount > account["Balance"]:
        print("Insufficient Balance!")
        return

    account["Balance"] -= amount
    account["History"].append(f"Withdrawn {amount}")

    print(f"{amount} Withdrawn Successfully.")


def check_balance():
    print(f"\nCurrent Balance : {account['Balance']}")


def transaction_history():

    if len(account["History"]) == 0:
        print("\nNo Transactions Till Now")
        return

    print("\n|| Transaction History ||")

    for transaction in account["History"]:
        print(transaction)


def change_pin():

    old_pin = int(input("Enter Current PIN : "))

    if old_pin != account["PIN"]:
        print("Wrong PIN")
        return

    new_pin = int(input("Enter New PIN : "))
    confirm = int(input("Confirm New PIN : "))

    if new_pin != confirm:
        print("PIN doesn't match.")
        return

    account["PIN"] = new_pin

    print("PIN Changed Successfully.")

print("|| WELCOME TO RBI ||")


acc = int(input("Enter Account Number : "))
pin = int(input("Enter PIN : "))

if acc != account["Account Number"] or pin != account["PIN"]:
    print("\nInvalid Account Number or PIN")
    exit()

print(f"\nWelcome {account['Name']}!")



while True:

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")
    

    choice = int(input("Enter Choice : "))

    if choice == 1:
        deposit()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        check_balance()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        change_pin()

    elif choice == 6:
        print("\n|| Thank You ||")
        break

    else:
        print("Invalid Choice!")