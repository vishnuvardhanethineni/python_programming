list_1=list(map(int,input().split()))
def duplicate_count():
    dic={}
    count=0
    for i in list_1:
        if i in dic:
            count+=1

        else:
            dic[i]=1
    print("Number of duplicate elements in the list are:",count)
duplicate_count()