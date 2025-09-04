def sum_n_naturalnumbers(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def prime_number(n):
    if n<=1:
        return 'not a prime number'
    else:
        for i  in range(2,int(n**0.5)+1):
            if n%i==0:
                print(i)
                return 'not a prime number'
        return 'prime number'
def mathametical_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
def sum_of_digits(n):
    s=0
    n=str(n)    
    for i in n:
        s+=int(i)
    return s
def count_digits(n):
    n=str(n)
    return len(n)
def first_and_last_digit(n):
    n=str(n)
    return int(n[0]),int(n[-1])
def sum_of_first_and_last_digit(n):
    n=str(n)
    return int(n[0])+int(n[-1])
def display_all_ascii_with_values():
    for i  in range(128):
        print(f"{i} : {chr(i)}")
def print_word(n):
    d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
    for i in str(n):
        print(d[int(i)],end=" ")
print(sum_n_naturalnumbers(10))
print(factorial(5))
print(prime_number(29))
mathametical_table(5)
print(sum_of_digits(12345))
print(count_digits(12345))
print(first_and_last_digit(12345))
print(sum_of_first_and_last_digit(12345))
display_all_ascii_with_values()
print_word(12345)