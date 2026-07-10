student1 = set()
student2 = set()

for i in range(1,5):
    subject = input(f"\nEnter Student1's Subject {i} : ")
    student1.add(subject)

for j in range(1,5):    
    subject = input(f"\nEnter Student2's Subject {j} : ")
    student2.add(subject)

x = student1.intersection(student2)
print("The common subjects are : ")
for  i in x:
    print(i)

y = student1.difference(student2).union(student2.difference(student1))

print("The different subjects are :")
for i in y:
    print(i)
