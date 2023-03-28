# Write a function named print_number_square that accepts a minimum and maximum integer and prints a square of lines of increasing numbers. The first line should start with the minimum, and each line that follows should start with the next-higher number. The sequence of numbers on a line wraps back to the minimum after it hits the maximum. For example, the call of print_number_square(3,7) should produce the following output:
#
# 3 4 5 6 7
# 4 5 6 7 3
# 5 6 7 3 4
# 6 7 3 4 5
# 7 3 4 5 6
#
# Write your function here
def print_number_square(min, max):
    for i in range(min, max + 1):
        for j in range(i, max + 1):
            print(j, end="")
        for j in range(min, i):
            print(j, end="")
        print()
