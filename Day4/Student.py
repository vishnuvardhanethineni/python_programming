class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")
student1 = Student("Alice", 101, 95)
student1.display()
student2 = Student("Bob", 102, 88)
student2.display()