# Wriet a function named triangle that accepts an integer parameter representing a size in characters, and prints to the console a right-aligned right triangle figure whose non-hypotenuse sides are that length, For example, the call of triangle(5) should print the following output:
#
#     *
#    **
#   ***
#  ****
# ***** 
#
# Write your function here
def triangle(size):
    for i in range(1, size + 1):
        for j in range(size - i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()