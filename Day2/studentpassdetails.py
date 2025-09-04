student_number=int(input("Enter your student number: "))
student_name = input("Enter your name: ")
math = int(input("Enter your math marks: "))
science = int(input("Enter your science marks: "))
english = int(input("Enter your english marks: "))
average=round((math+science+english)/3,2)
print("Student Details:")
print("Student Number:", student_number)
print("Name:", student_name)
print("Math Marks:", math)
print("Science Marks:", science)
print("English Marks:", english)
print("Average Marks:", average)
grade=None
if math>40 and science>40 and english>40:
    if average>=90:
        grade='A'
    elif average>=80:
        grade='B'
    elif average>60:
        grade='C'
    else:
        grade='D'
else:
    print("Student has failed in one or more subjects.")
print("Grade:", grade)