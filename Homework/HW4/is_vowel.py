# Write a function named is_vowel that returns whether a string is a vowel (a single-letter string containing a, e, i, o, or u, case-insensitively).

def is_vowel(string):
    if string == "a" or string == "A":
        return True
    elif string == "e" or string == "E":
        return True
    elif string == "i" or string == "I":
        return True
    elif string == "o" or string == "O":
        return True
    elif string == "u" or string == "U":
        return True
    else:
        return False