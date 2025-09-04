def display_prime_number(n):
    if n<=1:
        print('No prime numbers')
        return
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i,end=" ")
    print()
display_prime_number(20)