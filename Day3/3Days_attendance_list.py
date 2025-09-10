day1=['xyz@gmail.com','abc@gmail.com','pqr@gmail.com','lmn@gmail.com','stu@gmail.com','vish@gmail.com','var@gmail.com','hi@gmail.com','nan@gmail.com','stu@gmail.com','xyz@gmail.com']
day2=['xyz@gmail.com','abc@gmail.com','pqr@gmail.com','lmn@gmail.com','stu@gmail.com','vish@gmail.com','var@gmail.com','nan@gmail.com','stu@gmail.com','xyz@gmail.com']
day3=['xyz@gmail.com','abc@gmail.com','pqr@gmail.com','lmn@gmail.com','stu@gmail.com','vish@gmail.com','var@gmail.com','hi@gmail.com','stu@gmail.com','xyz@gmail.com']
for i in range(len(day1)):
    day1[i]=day1[i].lower()
for i in range(len(day2)):
    day2[i]=day2[i].lower()
for i in range(len(day3)):
    day3[i]=day3[i].lower()
day1=set(day1)
day2=set(day2)
day3=set(day3)
print("total number of attendees across all days : ",len(day1|day2|day3))
print("list of attendees who attended all three days : ",list(day1&day2&day3))
print("list of attendees who attended only day1 : ",list(day1-day2-day3))
print("overlap count Day1 and Day2 : ",len(day1&day2))
print("overlap count Day2 and Day3 : ",len(day2&day3))
print("overlap count Day1 and Day3 : ",len(day1&day3))
