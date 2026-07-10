class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = {}
        self.total = 0
        self.percentage = 0
        self.grade = ""
        self.result = ""

    def add_marks(self):
        n = int(input("Enter number of subjects: "))

        for i in range(n):
            subject = input(f"\nEnter Subject {i+1} Name: ")
            marks = float(input(f"Enter Marks in {subject}: "))
            self.subjects[subject] = marks

    def calculate_result(self):
        self.total = sum(self.subjects.values())
        self.percentage = self.total / len(self.subjects)

        if any(mark < 35 for mark in self.subjects.values()):
            self.result = "FAIL"
        else:
            self.result = "PASS"

        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B+"
        elif self.percentage >= 60:
            self.grade = "B"
        elif self.percentage >= 50:
            self.grade = "C"
        elif self.percentage >= 35:
            self.grade = "D"
        else:
            self.grade = "F"

    def display(self):
        print("\n" + "=" * 45)
        print("          STUDENT RESULT")
        print("=" * 45)
        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.roll_no}")
        print("-" * 45)

        print("Subject Marks")
        for subject, marks in self.subjects.items():
            print(f"{subject:<20} : {marks}")

        print("-" * 45)
        print(f"Total Marks : {self.total}")
        print(f"Percentage  : {self.percentage:.2f}%")
        print(f"Grade       : {self.grade}")
        print(f"Result      : {self.result}")
        print("=" * 45)


students = []

num_students = int(input("Enter Number of Students: "))

for i in range(num_students):
    print(f"\nEnter Details of Student {i+1}")

    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")

    student = Student(name, roll)

    student.add_marks()
    student.calculate_result()

    students.append(student)

print("\n\n||    ALL STUDENT RESULTS ||")

for student in students:
    student.display()


