def display_armstrong_numbers(n):
    for i in range(1,n+1):
        s=str(i)
        s1=0
        for j in s:
            s1+=(int(j)**len(s))
        if i==(s1):
            print(i,end=" ")
    print()
display_armstrong_numbers(1000)
            