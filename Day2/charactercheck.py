def character_check(char):
    if char.isalpha():
        return "Alphabet"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special Character"