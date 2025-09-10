def count_char(s):
    alpha = digit = special = 0
    for char in s:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1
    return alpha, digit, special
print(count_char("Hello123!@#"))
