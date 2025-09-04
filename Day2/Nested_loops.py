def print_pattern1():
    for _ in range(1,6):
        print("* "*5)

def print_pattern2():
    for i in range(1,6):
        for j in range(1,6):
            if i==j:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
def print_pattern3():
    for i in range(1,6):
        for j in range(1,6):
             if i==j or j==6-i:
                print("$",end=" ")
             else:
                print("*",end=" ")
        print()

print_pattern1()
print(10*"-")
print_pattern2()
print(10*"-")
print_pattern3()
