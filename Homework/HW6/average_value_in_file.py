# Write a function named average_value_in_file that accepts a file name as a parameter and reads that file, assumed to be full of numbers, and returns the average (mean) of the numbers in that file. The parameter, filename, gives the name of a file that contains a list of numbers, one per line. You may assume that the file exists and follows the proper format. For example, if a file named input.txt contains the following numbers

# 1.5
# 2.75
# 9.0
# -3.25
# 0.0
# 6.5
# Then the call of average_value_in_file("input.txt") should return 2.75.

# You may assume that the input file exists and is in the proper format. If the file does not contain any input values, return 0.0.

# Constraints: Your solution should read the file only once, not make multiple passes over the file data.

# Write your function here
def average_value_in_file(filename):
    file = open(filename, "r")
    sum = 0
    count = 0
    for line in file:
        sum += float(line)
        count += 1
    file.close()
    if count == 0:
        return 0.0
    return sum / count

    