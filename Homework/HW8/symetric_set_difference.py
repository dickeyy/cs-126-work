# Write a function named symmetric_set_difference that accepts two sets as parameters and returns a new set containing their symmetric set difference (that is, the set of elements contained in either of the two sets but not in both). For example, the symmetric difference between the sets {1, 4, 7, 9} and {2, 4, 5, 6, 7} is {1, 2, 5, 6, 9}. Do not call the set's symmetric_difference function in your solution.

def symmetric_set_difference(set1, set2):
    new_set = set()
    for e in set1:
        if e not in set2:
            new_set.add(e)
    for e in set2:
        if e not in set1:
            new_set.add(e)
    return new_set

    