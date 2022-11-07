# This program reads rating data, and then can recomemnd books to users or output the average rating for each book

# Define constants 
RATINGS_LIST = '' # Leave as empty sting for the long ratings, change to "-small" for the short ratings

# Define the main function
def main():
    # Call the gather_data function and store the returned values in variables
    user_ratings, books, book_ratings = gather_data()
    # Call the intro function
    intro(books, user_ratings, book_ratings)

# Define the gather_data function
def gather_data():
    # Open the file
    with open (f'./ratings{RATINGS_LIST}.txt', 'r') as f:
        first_list = f.readlines()
        # remove the newline character
        first_list = [line.strip() for line in first_list]

        # combine every three items in the list into one string and insert it into a new list
        new_list = []
        for i in range(0, len(first_list), 3):
            new_list.append(first_list[i] + ',' + first_list[i+1] + ',' + first_list[i+2])

        books = []
        book_ratings = {}
        users_ratings = {}

        # For each item in the new list, split the sting into a list of three items
        # the first item is the user, the second item is the book, and the third item is the rating
        # make a list of all the names of the books
        # then make a dictionary with the books as the keys, then a list of the respective books ratings for all users
        # then make a dictionary with the users as the keys, then a list of the respective users ratings for all books
        for item in new_list:
            item = item.split(',')
            books.append(item[1])
            if item[1] not in book_ratings:
                book_ratings[item[1]] = [item[2]]
            else:
                book_ratings[item[1]].append(item[2])
            if item[0] not in users_ratings:
                users_ratings[item[0]] = [item[2]]
            else:
                users_ratings[item[0]].append(item[2])

        # # remove duplicates from the list of books
        books = list(set(books))

        # Return the user_ratings dictionary and the list of books
        return users_ratings, books, book_ratings

# Define the intro function  
def intro(books, user_ratings, book_ratings):
    # Print the welcome message
    print('Welcome to the CS126 Book Recommender. Type the word in the\nleft column to do the action on the right.\n')
    print('recommend : recommend books for a particular user')
    print('averages : output the average ratings for all books in the system')
    print('quit : exit the program')
    # Call the recursive prompt function
    prompt(books, user_ratings, book_ratings)

# Define the prompt function, this function is recursive, meaning it can call itself
def prompt(books, user_ratings, book_ratings):
    # Prompt the user for input
    next_task = input('\nnext task?  ')
    print()

    # Determine what to do based on the user's input
    if next_task == 'recommend':
        recommend(books, user_ratings, book_ratings)
    elif next_task == 'averages':
        averages(books, user_ratings, book_ratings)
    elif next_task == 'quit':
        quit()
    else:
        print('Invalid input. Please try again.')
        prompt(books, user_ratings, book_ratings)

# Define the recommend function
def recommend(books, user_ratings, book_ratings):
    # First ask the user what user they want recommendations for
    r_user = input('Which user?  ')
    print()

    # If the user is not in the user_ratings dict, then print all the books available
    if r_user not in user_ratings:
        for book in books:
            print(book)
    else:

        r_user_ratings = user_ratings[r_user]

        # calculate the dot product between the user and every other users ratings
        dot_product = {}
        for user in user_ratings:
            if user != r_user:
                dot_product[user] = 0
                for i in range(len(user_ratings[user])):
                    try:
                        dot_product[user] += int(user_ratings[user][i]) * int(r_user_ratings[i])
                    except IndexError:
                        pass
        
        # Get the top 3 users with the highest dot product
        top_users = sorted(dot_product, key=dot_product.get, reverse=True)[:3]

        # create a new list the same length as the list of books and filled with 0s
        new_list = [0] * len(books)

        # loop through the list of books
        for i in range(len(books)):
            # loop through the first three users
            for user in top_users:
                # add up their ratings
                try:
                    new_list[i] += int(user_ratings[user][i])
                except IndexError:
                    pass
            # divide by the number of non-zero ratings
            try:
                new_list[i] = new_list[i] / len(top_users)
            except ZeroDivisionError:
                pass

        new_list = [(new_list[i], books[i]) for i in range(len(books)) if new_list[i] != 0]

        # sort this list
        new_list = sorted(new_list, key=lambda x: x[0], reverse=True)

        # print the top 5 books with their ratings, if there are less than 5 books, print all the books
        for i in range(5):
            try:
                print(new_list[i][1], round(new_list[i][0], 2))
            except IndexError:
                pass


    # Call the recursive prompt function
    prompt(books, user_ratings, book_ratings)


# Define the averages function
def averages(books, user_ratings, book_ratings):
    
    # For every item in the book_ratings dictionary, calculate the average rating for each book
    # then print the book name and the average rating

    av_list = []
    for book in book_ratings:
        average = sum(int(rating) for rating in book_ratings[book]) / len(book_ratings[book])
        av_list.append((average, book))

    # sort the list by the average rating
    av_list = sorted(av_list, key=lambda x: x[0], reverse=True)

    # print all the books and their average ratings
    for item in av_list:
        print(item[1], round(item[0], 2))
    
    # Call the recursive prompt function
    prompt(books, user_ratings, book_ratings)

# Define the quit function
def quit():
    print('Thank you! Goodbye.')

# Call the main function
main()