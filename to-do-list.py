print("|| TO_DO_LIST ||")

with open("to-do-list.txt",'r') as file:
    data = [line.strip() for line in file.readlines() if line.strip()]

def add_task():
    task = print("What task ? : ")
    data.append(task)

def view_list():
    for index, task in enumerate(data, start=1):
        print(f"{index}. {task}")

def save_tasks():
    with open("to-do-list.txt", "w") as file:
        for task in data:
            file.write(task + "\n")

def delete_task():
    view_list()
    if not data :
        print("The TO_FO LIST is empty")
    else:
        choice = int(input("Enter the number of task you want to remove : "))
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            save_tasks()
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number!")

while True:
    print("1.ADD TASK\n2.VIEW LIST\n3.DELETE TASK\n4.EXIT")
    choice = int(input("\nEnter The operation : "))
    
    if choice == 1:
        add_task()
    if choice == 2:
        view_list()
    if choice == 3:
        delete_task()
    if choice == 4:
        print("Exiting...")
        break
    else:
        print("INVALID INPUT !")