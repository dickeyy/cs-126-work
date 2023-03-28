# Write a function named vertical that accepts a string as its parameter and prints each letter of the string on seperate lines. For example, the call of vertical("hey now") should print the following output:
#
# h
# e
# y
#
# n
# o
# w
#
# Write your function here
def vertical(string):
    for i in range(len(string)):
        print(string[i])
        