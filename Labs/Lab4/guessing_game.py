import random

# Overall stats
total_games = 0
total_guesses = 0
best_game = 0

# Main function
def main(total_games, total_guesses, best_game):
    # Increment total games
    total_games += 1
    # Generate random number
    num = random.randint(1, 100)
    # Start game
    guesses = 0
    print("\nI'm thinking of a number between 1 and 100...")
    play_game(num, guesses, total_guesses, best_game, total_games)

# Play game function
def play_game(num, guesses, total_guesses, best_game, total_games):
    int(num)
    # Get user guess
    guess = int(input("Your guess? "))
    # If the guess is correct
    if guess == num:
        # Increment guesses
        guesses += 1
        # Increment total guesses
        total_guesses += guesses
        
        # If this is the best or first game
        if (guesses < best_game) or (best_game == 0):
            best_game = guesses

        # Report the win
        print("You got it right in " + str(guesses) + " guesses!")

        # Ask if the user wants to play again
        print("Would you like to play again? (y/n)")

        play_again = input()

        # If the user wants to play again
        if play_again[0].lower() == 'y':
            main(total_games, total_guesses, best_game)
        else:
            report_stats(total_games, total_guesses, best_game)
    
    # If the guess is too high
    elif guess < num:
        guesses+=1
        print("It's higher...")
        play_game(num, guesses,total_guesses, best_game, total_games)
        
    # if the guess is too low
    else:
        guesses+=1
        print("It's lower...")
        play_game(num, guesses, total_guesses, best_game, total_games)

# Report stats function
def report_stats(total_games, total_guesses, best_game):
    print('\nOverall results:')
    print('Total games =', total_games)
    print('Total guesses =', total_guesses)
    print('Guesses/game =', round(total_guesses / total_games, 1))
    print('Best game =', best_game)

# Run the main function
main(total_games, total_guesses, best_game)