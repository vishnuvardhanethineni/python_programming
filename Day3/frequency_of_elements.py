list_1=list(map(int,input().split()))
dic={}
for i in list_1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    print(f"{i} -> {dic[i]}")