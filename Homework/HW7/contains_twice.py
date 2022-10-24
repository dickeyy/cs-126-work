def contains_twice(string, char):
    num_occurrences = 0
    index = string.find(char)
    while index != -1:
        num_occurrences = num_occurrences + 1
        index = string.find(char, index + 1)

    return num_occurrences >= 2

print(contains_twice("banana", "a"))