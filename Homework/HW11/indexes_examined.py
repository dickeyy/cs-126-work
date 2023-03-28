# Suppose we are performing a binary search on a sorted list called numbers initialized as follows:

# # index     0   1   2   3   4   5   6   7   8   9  10  11  12  13
# numbers = []
# numbers += -23, -5,  9, 14, 15, 18, 23, 24, 25, 29, 34, 62, 85, 87
# index = binary_search(numbers, 25)
# Write the indexes of the elements that would be examined by the binary search (the mid values in our algorithm's code) and write the value that would be returned from the search.

# # <p> Now suppose we are performing both an iterative (loop-based) sequential search and then a recursive binary search on the same list. The sequential search is a standard version that does not take any advantage of the sortedness of the list, simply looking each element in order from the start to the end of the list. </p> <p> Suppose we are searching the list for the value 25. Also suppose that we are operating on a special computer where reading an element's value in the list (such as examining the value of numbers[0)] costs 7 units of time calling any function costs 10 units of time and all other operations are essentially 0 cost. What is the total "cost" of running a sequential search and recursive binary search over this list of data, searching for the value 25? </p>

# How many indexes are examined by the binary search? 3
# How many values are returned from the search? 1