class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print("Employee Details:")
        print(f"Name: {self.name}, Salary: ${self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        self.department=department
        super().__init__(name,salary)
    def display_info(self):
        print("Manager Details:")
        print(f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}")
emp1 = Employee("John", 50000)
emp1.display_info()
mgr1 = Manager("Jane", 80000, "Sales")
mgr1.display_info()