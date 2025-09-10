def search_occurance_chr(s,char):
    list1=[]
    for i in range(len(s)):
        if s[i]==char:
            list1.append(i)
    return list1
print(search_occurance_chr("hello world",'o'))