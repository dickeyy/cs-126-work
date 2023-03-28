# Write a function is_unique that accepts a dict from strings to strings as a parameter and returns True if no two keys map to the same value (and False if any two or more keys do map to the same value). For example, calling your function on the following dictionary would return True:

# {Marty=Stepp, Stuart=Reges, Jessica=Miller, Amanda=Camp, Hal=Perkins
# Calling it on the following dictionary would return False, because of two mappings for Perkins and Reges:

# {Kendrick=Perkins, Stuart=Reges, Jessica=Miller, Bruce=Reges, Hal=Perkins
# The empty dictionary is considered to be unique, so your function should return True if passed an empty dictionary.

# Write your function here
def is_unique(map):
    values = []
    for k in map.keys():
        if map[k] in values:
            return False
        else:
            values.append(map[k])
    return True
    