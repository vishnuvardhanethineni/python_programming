def display_all_factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
    print()
def display_prime_factors(n):
    if n<=1:
        print('No prime factors')
        return
    for i in range(2,n+1):
        if n%i==0:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                print(i,end=" ")
    print()
display_all_factors(28)
display_prime_factors(28)