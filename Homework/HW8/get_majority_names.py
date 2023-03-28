# Write a function named get_majority_last_name that accepts as its parameter a dictionary from strings to strings the keys of the dictionary represent first names and the values represent last names. If there is a single common last name that is present in more than half of the key/value pairs in the dictionary passed in (a "majority" last name), your function should return that last name. If there is no majority last name, your function should return the string "?" .

# For example, if the dictionary contains the following key/value pairs, the majority last name is "Smith" because it occurs 5 times, which is more than half of the nine pairs in the dictionary. Therefore your function would return "Smith".

# {'Hal': 'Perkins', 'Mark': 'Smith', 'Mike': 'Smith', 'Stuart': 'Reges', 'David': 'Smith',
#  'Jean': 'Reges', 'Geneva': 'Smith', 'Amie': 'Smith', 'Bruce': 'Reges'}
# The following dictionaries don't have any majority last name because no last name occurs strictly greater than half the time. Therefore when passed either of the dictionaries below, your function would return "?" .

# {'Marty': 'Stepp', 'Mehran': 'Sahami', 'Keith': 'Schwarz', 'Cynthia': 'Lee', 'Yogurt': 'Schwarz',
#  'Tywin': 'Lannister', 'Rob': 'Stark', 'Sansa': 'Stark', 'Tyrion': 'Lannister'}
# If the dictionary that contains only one key/value pair, that pair's value is the majority last name. An empty dictionary does not have any majority last name.

# Constraints: You may declare at most one auxiliary collection to help you solve this problem. Do not modify the map that is passed in to your function as a parameter.

# Write your function here
def get_majority_last_name(map):
    last_names = {}
    for k in map.keys():
        if map[k] in last_names:
            last_names[map[k]] += 1
        else:
            last_names[map[k]] = 1
    max_count = 0
    max_name = "?"
    for k in last_names.keys():
        if last_names[k] > max_count:
            max_count = last_names[k]
            max_name = k
    if max_count > len(map) / 2:
        return max_name
    else:
        return "?"

        