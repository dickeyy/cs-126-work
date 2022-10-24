import math
from turtle import *
from Lab5_functions import *

# Define main function
def main():
    # Print the intro
    print('This progaram allows you to search through\ndata about congressional voting districts\nand determine whether a particular state is\ngerrymandered.\n')
    # Call get_state
    get_state()

# Define get_state
def get_state():
    # Get the input
    state_input = input("Which state do you want to look up? ")

    # Format the input
    state_input.lower()
    state = state_input.title()

    # Open the files
    with open('districts.txt') as f:
        with open('eligible_voters.txt') as f2:
            # find the state in eligible_voters.txt
            for line2 in f2:
                if state in line2:
                    split2 = line2.split(",")[1]
                    # format the data
                    eligible_voters = split2.split('\n')[0]
                    break
            # find the state in districts.txt
            for line in f:
                if state in line:
                    state = line
                    
                    # format the data
                    split = state.split(',')
                    split.pop(0)

                    # Define the inital variables
                    districts = 0
                    total_wasted_dem = 0
                    total_wasted_rep = 0
                    total_dem_votes = 0
                    total_rep_votes = 0

                    # Loop through the data
                    for i in range(len(split)):

                        if i % 3 == 0:
                            districts += 1
                            
                            dem_votes = int(split[i+1])
                            rep_votes = int(split[i+2])
                            total_dem_votes += dem_votes
                            total_rep_votes += rep_votes

                            if dem_votes > rep_votes:
                                wasted_dem = math.ceil(((dem_votes - rep_votes) / 2) + 1)
                                wasted_rep = rep_votes

                            else:
                                wasted_rep = math.ceil(((rep_votes - dem_votes) / 2) + 1)
                                wasted_dem = dem_votes
                            
                            total_wasted_dem += wasted_dem
                            total_wasted_rep += wasted_rep
                    
                    print(f'Total Wasted Democratic votes: {total_wasted_dem}')
                    print(f'Total Wasted Republican votes: {total_wasted_rep}')

                    if (total_wasted_dem > total_wasted_rep):
                        print("Gerrymandered beneiting the Republicans")
                    else:
                        print("Gerrymandered beneiting the Democrats")
                    
                    print(f'{eligible_voters} eligible voters')
                    
                    draw_results(total_dem_votes, total_rep_votes, eligible_voters, districts, state_input.title())

                    break
            else:
                print(f'"{state_input} not found.')
                get_state()


def draw_results(dem_votes, rep_votes, eligible_voters, districts, state):
    
   
    speed('fastest')
    height = 500
    width = 500
    screen = Screen()
    screen.screensize(250, 250)
    pen_state = pen()

    draw_line(-250, 0, 250, 0, 'black')
    draw_line(0, -250, 0, 250, 'black')

    write(state, move=False, align="right", font=("Arial", 16, "normal",))
    write('Eligible Voters: ' + eligible_voters, move=False, align="left", font=("Arial", 16, "normal",))

    for i in range(districts):
        draw_rect(-250, -250 + (i * 50), 20, (dem_votes/(dem_votes + rep_votes) * 500), 'blue')
        draw_rect(-250, -250 + (i * 50), 20, (rep_votes/(rep_votes + dem_votes) * 500), 'red')

    Screen().exitonclick()

main()

# My partner didn't help with any of this lab. I know that the turtle part is not right, but I don't have time to fix it