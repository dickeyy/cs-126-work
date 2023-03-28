# Write a function named binary_boarding that finds the highest seat ID on any boarding pass on an airplane using a specific algorithm described below. Your function reads data from an input file where each line contains a seat specification as a sequence of 10 characters:

# FBFBBFFRLR
# BFFFBBFRRR
# BBFFBBFRLL
# FFFBBBFRRR
# The first 7 characters describe movements toward the front or back of the plane between rows, and the last 3 characters describe movements left or right within the row. An example seat specification is FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right". The airplane has 128 rows (numbered 0 through 127 from front to back) and 8 columns of seats in each row (numbered 0 through 7 from left to right). For the first seven letters of a seat specification, each letter tells you which half of a region of rows the given seat is in. Start with the whole list of rows the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of the seat FBFBBFFRLR: Start by considering the whole range, rows 0 through 127. And then:

# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B means to take the upper half, keeping rows 44 through 47.
# F means to take the lower half, keeping rows 44 through 45.
# F means to take the lower half, keeping row 44.
# The last three characters will be either L or R these specify one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half. For example, consider just the last 3 characters of FBFBBFFRLR. Start by considering the whole range, columns 0 through 7. And then:

# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# R means to take the upper half, keeping column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# To compute a seat's unique seat ID, multiply the row by 8, then add the column. In this example, the seat has an ID of 44 * 8 + 5 = 357.

# The goal of your function is to find and return the highest seat ID found in the input data. For the input data above, the highest seat ID comes from BBFFBBFRLL, which corresponds to row 102, column 4, with a seat ID of 820. So the call of binary_boarding("boarding.txt") would return 820.

# You may assume that the file exists and is readable, that it follows the general format described above, and that it contains at least one seat specification.

def binary_boarding(filename):
    """Reads a file of boarding passes and returns the highest seat ID."""
    with open(filename) as f:
        highest = 0
        for line in f:
            line = line.strip()
            row = binary_search(line[:7], 0, 127)
            col = binary_search(line[7:], 0, 7)
            seat_id = row * 8 + col
            if seat_id > highest:
                highest = seat_id
        return highest
    
def binary_search(spec, low, high):
    """Returns the row or column number for a seat."""
    if spec == "":
        return low
    elif spec[0] == "F" or spec[0] == "L":
        return binary_search(spec[1:], low, (low + high) // 2)
    else:
        return binary_search(spec[1:], (low + high) // 2 + 1, high)