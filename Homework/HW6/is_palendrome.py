# Write a function is_palindrome that accepts a list of strings as its argument and returns True if that list is a palindrome (if it reads the same forwards as backwards) and False if not. For example, the list ["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"] is a palindrome, so passing that list to your function would return True. Lists with zero or one element are considered to be palindromes.

# Write your function here
def is_palindrome(a):
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True