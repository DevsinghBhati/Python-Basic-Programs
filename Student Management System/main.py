import json

student_dict = {}
with open("student-list.json","r") as file:
    student_dict = json.load(file)

def save_data():
        with open("student-list.json", "w") as file:
            json.dump(student_dict, file, indent=4)


def Add():
    name = input("Enter your name: ")
    roll_no = int(input("Enter roll number : "))
    student_dict[name] = {
            "name": name,
            "roll-no" : roll_no
    }
    print("Student Added Successfully")
    save_data()

def view():
    if not student_dict:
        print("No students found.")
    else:
        print("NAME : ROLE NUMBER")
        for name, data in student_dict.items():
            print(f"{data['name']} : {data['roll-no']}")
                  

def delete():
    name = input("Enter the name of the student to delete: ")
    if name in student_dict:
        del student_dict[name]
        save_data()
        print(f"Student '{name}' deleted successfully.")
    else:
        print("Student not found.")

    sace_data()

while True:
    choice = int(input("\n1.ADD STUDENT\n2.VIEW STUDENT\n3.DELETE STUDENT\n4.EXIT\nEnter your operation: "))
    if choice == 1:
        Add()
    if choice == 2:
        view()
    if choice ==3:
        delete()
    if choice == 4:
        break
    if 1 < choice > 4:
        print("INVALID INPUT!")

print("Exiting...")