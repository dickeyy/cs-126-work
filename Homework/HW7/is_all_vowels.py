def is_all_vowels(string):

    # Initialize the vowel count
    vowel_count = 0

    # Loop through the string
    for char in string:
        # Check if the character is a vowel
        if char in 'aeiouAEIOU':
            # Increment the vowel count
            vowel_count = vowel_count + 1

    # Check if the vowel count is equal to the length of the string
    if vowel_count == len(string):
        # Return True
        return True
    else:
        # Return False
        return False