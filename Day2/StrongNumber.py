def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def display_strong_numbers(n):
    for i in range(1,n+1):
        s=str(i)
        s1=0
        for j in s:
            s1+=factorial(int(j))
        if i==s1:
            print(i,end=" ")
    print()
display_strong_numbers(500)