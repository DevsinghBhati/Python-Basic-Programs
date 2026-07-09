number_of_students = int(input("\nEnter number of Students : "))

studentlist = {}
for  i in range(number_of_students):
    name = input(f"Enter the name of Student {i+1} : ").capitalize()
    studentlist[name] = 0

names = studentlist.keys()
for i in studentlist:
    
    choice = input(f"Is {i} present ? (y/n) : ").lower()
    if choice == 'y':
        studentlist.update({i:1})

count = 0
for i in studentlist:
    if studentlist[i] == 1:
        count += 1

percent = (count/number_of_students)*100

print(f"Total students are {number_of_students}")
print("The number of present student is : ", count)
print(f"The percentage ratio is : {percent} %")