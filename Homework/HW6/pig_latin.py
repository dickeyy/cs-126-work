# Write a function named pig_latin that accepts as a parameter a string representing an input file name. Your function should, preserving line breaks, prout the input file's text in a simplified version of Pig Latin, a silly English variant where the first letter of each word is moved to the end. The rules for translating a word to Pig Latin are as follows:

# If the word starts with a vowel (aeiou), simply append "yay". For example, "elephant" becomes "elephantyay".
# If the word starts with a consonant, move the consonant to the end, and append "ay". For example, "welcome" becomes "elcomeway".
# As an overall example, if the input file lincoln.txt contains the following text:

# four score and
# seven years ago our
# fathers brought forth on this continent a new nation
# The call of pig_latin("lincoln.txt") should produce the following output:

# ourfay coresay andyay
# evensay earsyay agoyay ouryay
# athersfay roughtbay orthfay onyay histay ontinentcay ayay ewnay ationnay

# Write your function here
def pig_latin(filename):
    file = open(filename, "r")
    for line in file:
        words = line.split()
        for word in words:
            if word[0] in "aeiou":
                print(word + "yay", end=" ")
            else:
                print(word[1:] + word[0] + "ay", end=" ")
        print()
    file.close()