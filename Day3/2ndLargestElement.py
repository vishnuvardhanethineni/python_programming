list_1=[2,4,6,8,10]
def second_largest():
    maxi=float('-inf')
    second_maxi=float('-inf')
    for i in list_1:
        if i>maxi:
            second_maxi=maxi
            maxi=i
    return second_maxi
print(second_largest())