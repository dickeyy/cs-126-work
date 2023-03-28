# Write a function that accepts two non-negative integers and returns True if the first integer is a multiple of the second integer. Otherwise, it returns False.

def is_multiple(x, y):
    if x % y == 0:
        return True
    else:
        return False
        