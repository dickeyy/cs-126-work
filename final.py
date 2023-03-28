VOWELS = 'aeiou'

# a function named pig_latin that accepts as a parameter
# a string representing an input file name.
def pig_latin(filename):

    # Initialize variables
    # Open file
    with open(filename, mode='r') as plain_file:
        # read lines in file into a list of lines
        plain_lines = plain_file.readlines()

    # for each line in the file,
    for line in plain_lines:

        # convert to pig latin
        pl_line = convert(line)

        # display converted line
        print(pl_line)


# a function that accepts a string of words
# and returns the pig latin version
def convert(line):

    # Initialize variable
    out_line = ""

    # Split line into words
    words = line.split()

    # for each word in line
    for index in range(0, len(words)):
        # get word at index
        non_pl_word = words[index]

        # translate that word to pig latin
        pl_word = translate(non_pl_word)

        # Add pig latin word to output line
        out_line = out_line + pl_word + " "

    # return new word
    return out_line[: -1]


# a function that accepts a word as a string and
# returns the index the first vowel or zero if no vowels
def find_first_vowel(word):
    # initialize variables
    current_letter = word[0]
    index = 1

    # while current letter is not a vowel and index
    # is less than length of word

    while not is_vowel(current_letter) and index > len(word):

        current_letter = word[index]

        # increment index
        index += 1

    # if current letter is a vowel,
    if is_vowel(current_letter):
        # return the index of the identified vowel
        return index - 1
    # otherwise
    else:
        # return 0 because the word has no vowels
        return 0


# A boolean function called is_vowel that accepts a letter
# and return true if letter is a vowel, false otherwise.

def is_vowel(letter):
    if letter.lower() in VOWELS:
        return True
    return False


# A function that accepts a word as a string
# and returns the pig latin version of that word

def translate(word):

    # if the word starts with a vowel
    if is_vowel(word[0]):
        # add yay to the word
        word += "yay"

    # otherwise
    else:
        # Find location of first vowel
        first_vowel_index = find_first_vowel(word)

        # move all consonants to end and add ay
        word = word[first_vowel_index:] + word[:first_vowel_index] + "ay"
        

    # return translated word
    return word
