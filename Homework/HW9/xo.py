# Write a function named xo that accepts an integer size as a parameter and prints a square of size by size characters, where all characters are "o" except that an "x" pattern of "x" characters has been drawn from the corners of the square. In other words, on the first line, the first and last characters are "x"; on the second line, the second and second-from-last characters are "x"; and so on. If 0 or less is passed for the size, no output should be produced

# Write your function here:
def xo(size):

    if size <= 0:
        return

    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("x", end = "")
            else:
                print("o", end = "")
        print()

xo(5)