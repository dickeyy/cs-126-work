# Write a function named pig_latin2 that is a modified version of the preceding pig_latin problem. In this modified version, if the word starts with constants, move all constants up to the first vowel (not just the first consonant) to the end, and append "ay". For example, the word "scram" would become "amscray".

def pig_latin2(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"