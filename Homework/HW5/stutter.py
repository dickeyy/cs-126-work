# Write a function named stutter that accepts a string parameter returns a new string replacing each of its characters with two consecutive copies of that character. For example, A call of stutter("hello") would return "hheelllloo".

# Write your function here
def stutter(string):
    new_string = ""
    for i in range(len(string)):
        new_string += string[i] * 2
    return new_string
