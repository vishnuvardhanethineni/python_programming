def occurence_char(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    s=''
    for i in dic:
        s+=i+str(dic[i])
    print(s)
occurence_char("helloworld")