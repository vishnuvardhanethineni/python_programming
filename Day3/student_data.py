list1=[]
def student_info(roll_no,name,marks):
    list1.append((roll_no,name,marks))
student_info(1,"Alice",85)
student_info(2,"Bob",90)
student_info(3,"Charlie",68)
student_info(4,"David",92)
student_info(5,"Eve",92)
def highest_scorer():
    marks=max(list1,key=lambda x:x[2])
    for i in list1:
        if marks[2]==i[2]:
            print(f"Highest scorer Name: {i[1]}")
def marks_above_75():
    for i in list1:
        if i[2]>75:
            print(f"Roll No: {i[0]}, Name: {i[1]}, Marks: {i[2]}")
highest_scorer()
marks_above_75()