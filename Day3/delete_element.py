list_1=list(map(int,input().split()))
def delete_element():
    element=int(input("Enter the element to be deleted: "))
    ind=-1
    for i in range(len(list_1)):
        if i==element:
            ind=i 
            break
    if ind!=-1:
        for i in range(ind,len(list_1)-1):
            list_1[i]=list_1[i+1]
    return list_1[:-1]
print(delete_element())