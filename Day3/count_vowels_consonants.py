def count_vowels_consonants(s):
    vowels=consonants=0
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels+=1
            else:
                consonants+=1
    return f"Vowels: {vowels}, Consonants: {consonants}"
print(count_vowels_consonants("Hello World!"))