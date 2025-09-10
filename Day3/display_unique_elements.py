list_1=list(map(int,input().split()))
print("Unique elements in the list are:", set(list_1))
#another method
dic={}
for i in list_1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print("Unique elements in the list are:", list(dic.keys()))