def even_and_odd_count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2:
            odd+=1
        else:
            even+=1
    return f"Even count: {even}, Odd count: {odd}"
print(even_and_odd_count([1,2,3,4,5,6,7,8,9,10]))