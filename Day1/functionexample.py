def fun(name,rollnumber):
    print(f"name={name} and rollnumber={rollnumber}")
fun("vishnu",101)
fun("ajay",102)
def fun1(*name):
    for i in name:
        print(i)
fun1('abc','def','ghi','jkl')
def convertdaytomonthandyear(days):
    years=days//365
    months=(days%365)//30
    remaining_days=(days%365)%30
    return years,months,remaining_days
convertdaytomonthandyear(400)
def returnvalues():
    return 10,20,30
print(returnvalues())
def multiply(a,b):
    return a*b
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def rounddivision(a,b):
    return a//b
def modulus(a,b):
    return a%b
def exponent(a,b):
    return a**b
multiply(10,20)
add(10,20)
subtract(20,10)
divide(20,10)
rounddivision(10,5)
modulus(10,3)
exponent(2,3)
def checkevenorodd(num):
    if num<0:
        return "Invalid input"
    return num%2==0
print(checkevenorodd(10))
def checkpositiveornegative(num):
    if num<0:
        return "Negative"
    elif num>0:
        return "Positive"
    else:
        return "Zero"
print(checkpositiveornegative(-10))
def checkdivisibleby5and11(num):
    return num%5==0 and num%11==0
print(checkdivisibleby5and11(55))
def checkleapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"
print(checkleapyear(2020))
def checkalphabet(char):
    return char.isalpha() # or return (char>='a' and char<='z') or (char>='A' and char<='Z')
print(checkalphabet('a'))
def checkvowelorconsonant(char):
    if char in 'aeiouAEIOU':
        return "Vowel"
    else:
        return "Consonant"
print(checkvowelorconsonant('b'))
def findlargest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
print(findlargest(10,20,30))