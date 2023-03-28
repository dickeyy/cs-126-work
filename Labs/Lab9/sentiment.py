# This program takes a file and processes it to determine the sentiment of the words in the file

# Define main function
def main():
    # Get the name of the file to analyze.
    filename = input('Learning data file name? ')
    # analyze the file
    data = analyze_file(filename)
    # ask what the user wants to do
    prompt(data)

# Define the analyze file function
def analyze_file(filename):

    # OPEN THE FILE 
    with open(filename, 'r') as f:
        # READ THE FILE
        lines = f.readlines()
        # CREATE A DICTIONARY TO STORE THE DATA
        data = {}
        
        for line in lines:
            # split line into individual words
            words = line.split()

            # get the score
            line_score = int(words[0])

            # remove the score from the words list
            words = words[1:]

            # Remove punctuation from the words
            for i in range(len(words)):
                words[i] = words[i].strip(',.?!')

            # loop through the words
            for word in words:
                word = word.lower()
                # if the word is not in the dictionary, add it
                if word not in data:
                    data[word] = {'count': 0, 'scores': []}
                # Count how many times the word appears, and also keep track of the score of the line it is in
                data[word]['count'] += 1
                data[word]['scores'].append(line_score)

        # calculate the average score for each word
        for word in data:
            data[word]['average'] = round(sum(data[word]['scores']) / data[word]['count'], 2)

        # Calculate the average score for the entire file
        total = 0
        for word in data:
            total += data[word]['average']
        file_average = total / len(data)
        data['totalFileAverage'] = file_average

        # For each word, if the word average is above the file average, add positive: True to the dictionary
        for word in data:
            if word != "totalFileAverage":
                if data[word]['average'] > file_average:
                    data[word]['positive'] = True
                elif data[word]['average'] < file_average:
                    data[word]['positive'] = False

    return data

# Define the prompt function
def prompt(data):
    # List the options for the program
    print('What would you like to do?')
    print('1: Get the score of a word')
    print('2: Get the average score of words in a file')
    print('3: FInd the highest / lowest scoring words in a file')
    print('4: Sort the words in a file into positive.txt and negative.txt')
    print('5: Exit the program')
    # Ask what the user wants to do
    choice = input('Enter a number 1 - 5: ')

    # Process choice
    if choice == '1':
        get_score_of_word(data)
    elif choice == '2':
        get_average_score(data)
    elif choice == '3':
        get_highest_lowest(data)
    elif choice == '4':
        sort_into_files(data)
    elif choice == '5':
        print('Goodbye!')
        return
    else:
        print('Invalid choice')
        prompt(data)

# Define get score of word function
def get_score_of_word(data):
    # Ask the user for a word
    word = input("Which word? ")
    word = word.lower()

    # Check if the word is in the dictionary
    if word in data:
        print(f"Score = {data[word]['average']}")
        if data[word]['positive']:
            print(f'{word} is positive')
        else: 
            print(f'{word} is negative')
    else:
        print("Word not found")
    
    print()

    prompt(data)

# Define the get average score function
def get_average_score(data):
    # Ask the user for a file name
    file = input("File name? ")
    # Open the file
    with open(file, 'r') as f:
        lines = f.readlines()
        total = 0
        # Loop through the lines in the file
        for line in lines:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in data:
                    total += data[word]['average']
        average = total / len(data)
        print(f"Average Score = {average}")
        if average > data['totalFileAverage']:
            print(f"{lines[0]} \nis positive")
        else:
            print(f"{lines[0]} \nis negative")

        is_right = input("Am I right (yes/no)? ")
        if is_right == 'yes':
            print("Yay!")
        else:
            user_score = input("What score should this sentence have (0 - 4 where 4 is the most positive)? ")
            words = lines[0].split()

            for word in words:
                word = word.lower()
                if word not in data:
                    data[word] = {'count': 0, 'scores': []}
                data[word]['count'] += 1
                data[word]['scores'].append(int(user_score))

    print()
    prompt(data)

# Define the get highest / lowest scoring words function
def get_highest_lowest(data):
    file = input("File name? ")
    with open(file, 'r') as f:
        lines = f.readlines()
        highest = 0
        lowest = 4
        highest_word = ''
        lowest_word = ''
        for line in lines:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in data:
                    if data[word]['average'] > highest:
                        highest = data[word]['average']
                        highest_word = word
                    if data[word]['average'] < lowest:
                        lowest = data[word]['average']
                        lowest_word = word
        print(f"Highest scoring word: {highest_word} ({highest})")
        print(f"Lowest scoring word: {lowest_word} ({lowest})")

    print()
    prompt(data)

def sort_into_files(data):
    positive_file = open('positive.txt', 'w')
    negative_file = open('negative.txt', 'w')

    # Loop through the data dictionary
    for word in data:
        if word != "totalFileAverage":
            if data[word]['positive'] == True:
                positive_file.write(f"{word}\n")
            else:
                negative_file.write(f"{word}\n")

    print()
    prompt(data)

# Call the main function
main()