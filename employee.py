class employee:
    def __init__(self , name, emp_salary):
        self.name = name
        self.emp_salary = emp_salary
    def salary(self):
        return self.emp_salary
    
class manager(employee):
    def __init__(self, name, emp_salary, bonus):
        super().__init__(name, emp_salary)
        self.bonus = bonus 
    def salary(self):
        return self.emp_salary + self.bonus
    
employes = employee("Dev",30000)
manager_1 = manager("Hariom Bhaiya", 50000,20000)

print(f"{employes.name} has {employes.salary()}")
print(f"{manager_1.name} has {manager_1.salary()}")