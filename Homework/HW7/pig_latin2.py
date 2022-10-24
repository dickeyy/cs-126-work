def pig_latin(input_file_name):

    with open(input_file_name) as input_file:
        for line in input_file:
            line = line.strip().split()

            # initialize the output list
            output_list = []

            # loop through the words in the line
            for word in line:
                # check if the word starts with a vowel
                if word[0] in 'aeiou':
                    # add the word to the output list
                    output_list.append(word + 'way')
                else:
                    # add the word to the output list
                    output_list.append(word[1:] + word[0] + 'ay')

            # print the output list
            print(' '.join(output_list))

pig_latin('/Users/kyledickey/Documents/Code/cs-126-homework/Homework/HW7/test.txt')

def pig_latin2(input_file_name):

    with open(input_file_name) as input_file:
        for line in input_file:
            line = line.strip().split()

            # initialize the output list
            output_list = []

            # loop through the words in the line
            for word in line:
                # check if the word starts with a vowel
                if word[0] in 'aeiou':
                    # add the word to the output list
                    output_list.append(word + 'way')
                else:
                    for i in range(len(word)):
                        # move every letter until you get to a vowel to the end
                        if word[i] in 'aeiou':
                            break
                        else:
                            output_list.append(word[i:] + word[:i] + 'ay')

            # print the output list
            print(' '.join(output_list))

# THIS DOESNT WORK