def perfect_numbers(n):
    if n<=0:
        print('No perfect numbers')
        return
    for i in range(1,n+1):
        s=0
        for j in range(1,i):
            if i%j==0:
                s+=j
        if s==i:
            print(i,end=" ")
    print()
perfect_numbers(1000)