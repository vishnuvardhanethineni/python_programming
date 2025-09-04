def display_palindrome_numbers(n):
    for i in range(1,n+1):
        s=str(i)
        if s==s[::-1]:
            print(i,end=" ")
    print()
display_palindrome_numbers(100)