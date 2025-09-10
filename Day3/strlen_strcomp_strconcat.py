def lenstr(s):
    count = 0
    for char in s:
        count += 1
    return count
print(lenstr("Hello, World!"))
def compare_strings(s1,s2):
    if s1==s2:
        return "Equal"
    elif s1>s2:
        return f"{s1} is greater than {s2}"
    else:
        return f"{s1} is less than {s2}"
print(compare_strings("apple","banana"))
def concat_strings(s1,s2):
    return s1+s2
print(concat_strings("Hello, ","World!"))
