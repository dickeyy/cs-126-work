# The following function attempts to return the median (middle) of three integer values, but it contains logic errors. In what cases does the function return an incorrect result? How can the code be fixed? Determine what is wrong with the code, and submit a corrected version that works properly.

# def median_of_3(n1, n2, n3):
#     if n1 < n2:
#         if n2 < n3:
#             return n2
#         else:
#             return n3
#     else:
#         if n1 < n3:
#             return n1
#         else:
#             return n3

# Correct the code
def median_of_3(n1, n2, n3):
    if n1 < n2:
        if n2 < n3:
            return n2
        else:
            if n1 < n3:
                return n3
            else:
                return n1
    else:
        if n1 < n3:
            return n1
        else:
            if n2 < n3:
                return n3
            else:
                return n2