# Write a function named words_between that accepts a file name as a parameter. Your function should read a sorted dictionary from that file, then prompt the user for two words and tell the user how many words in the dictionary fall between those two words. Here is a sample run of the program:

# Type two words: goodbye hello
# There are 4418 words between goodbye and hello

# Write your function here
def words_between(file_name):
    file = open(file_name, 'r')
    words = file.read().split()
    file.close()
    word1 = input('Type two words: ').split()[0]
    word2 = input('Type two words: ').split()[1]
    word1_index = words.index(word1)
    word2_index = words.index(word2)
    print('There are', word2_index - word1_index - 1, 'words between', word1, 'and', word2)