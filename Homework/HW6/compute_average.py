# Write a function named compute_average that computes and returns the mean of all elements in a list of integers. For example, if a list named a contains [1, -2, 4, -4, 9, -6, 16, -8, 25, -10], then the call of compute_average(a) should return 2.5.

# Constraints: You may assume that the list contains at least one element. Your function should not modify the elements of the list.

# Write your function here
def compute_average(a):
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)
    