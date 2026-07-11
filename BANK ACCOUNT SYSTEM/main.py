import random
import json 

total_dict = {}
with open("bank-system.json", "r") as file:
    total_dict = json.load(file)
account = {}

class bank:

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def create_account():
        global account
        name = input("\nEnter your name:")
        x = random.randint(111111, 999999)
        account_number = x
        print(f"{account_number} is your account number ")
        pin = int(input("Enter 4 digit pin : "))
        balance = 0
        print(f"Your initial bank balance is now {balance}")

        str_acc_num = str(account_number)

        total_dict[str_acc_num] = {
            "Account Number": int(account_number),
            "PIN": pin,
            "Name": name,
            "Balance": balance,
            "History": [],
        }
        account = total_dict[str_acc_num]
        bank.save_data()

    def deposit():
        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        account["Balance"] += amount
        account["History"].append(f"Deposited  {amount}")

        total_dict[str(account["Account Number"])] = account
        bank.save_data()

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
        total_dict[str(account["Account Number"])] = account
        bank.save_data()

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
        total_dict[str(account["Account Number"])] = account
        bank.save_data()
        print("PIN Changed Successfully.")

    def save_data():
        with open("bank-system.json", "w") as file:
            json.dump(total_dict, file, indent=4)

print("|| WELCOME TO RBI ||")

acc = int(input("Enter Account Number : "))
pin = int(input("Enter PIN : "))

str_acc = str(acc)

if str_acc in total_dict and total_dict[str_acc]["PIN"] == pin:
    account = total_dict[str_acc]
else:
    print("\nInvalid Account Number or PIN")
    print("let's create an account >>> ")
    bank.create_account()

print(f"\nWelcome {account['Name']}!")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        bank.deposit()

    elif choice == 2:
        bank.withdraw()

    elif choice == 3:
        bank.check_balance()

    elif choice == 4:
        bank.transaction_history()

    elif choice == 5:
        bank.change_pin()

    elif choice == 6:
        print("\n|| Thank You ||")
        break

    else:
        print("Invalid Choice!")