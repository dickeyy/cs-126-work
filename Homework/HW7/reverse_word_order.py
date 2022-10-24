def reverse_word_order(s):
    # split the string into a list of words
    word_list = s.split()
    # reverse the list
    word_list.reverse()
    # join the list into a string
    return ' '.join(word_list)