# This program takes a variety of grade inputs and calculates the final grade

# Define main function
def main():
    # Run the intro function to print the intro
    initialize()
    # Run the midterm_1 function to get the midterm_1 grade
    midterm_1_grade = midterm_1()
    # Run the midterm_2 function to get the midterm_2 grade
    midterm_2_grade = midterm_2()
    # Run the final_test function to get the final_test grade
    fina_test_grade = final_test()
    # Run the homework function to get the homework grade
    homework_grade = homework()
    # Run the calculate_grade function to get the final grade
    calculate_grade(midterm_1_grade,midterm_2_grade,fina_test_grade,homework_grade)

# Define the intro function
def initialize():
    # Print the intro
    print("This program reads exam/homework scores\n and reports your overall course grade.")
    print()

# Define the midterm_1 function
def midterm_1():
    # Print the intro
    print("Midterm 1:")
    # Request the weight of the midterm
    print("Weight (0-100)? ")
    weight = int(input())
    # Request the score earned on the midterm
    print("Score earned? ")
    score = int(input())
    # Request if the scores were shifted
    print("Were scores shifted (1=yes, 2=no)? ")
    shift = int(input())
    # If the scores were shifted, request the shift amount
    if shift == 1:
        print("Shift amount? ")
        shift_amount = int(input())
        # Add the shift amount to the score
        score = score + shift_amount
        
        # If the score is greater than 100, restrict it to 100
        if score > 100:
            score = 100

    # Print the total points and calculate weighted score
    print("Total points = ", score, " / 100")
    print("Weighted score = ", round(score * weight / 100, 1), " / ", weight)
    print()

    # Return the weighted score
    return (score * weight / 100)

# Define the midterm_2 function
def midterm_2():
    # Print the intro
    print("Midterm 2:")
    # Request the weight of the midterm
    print("Weight (0-100)? ")
    weight = int(input())
    # Request the score earned on the midterm
    print("Score earned? ")
    score = int(input())
    # Request if the scores were shifted
    print("Were scores shifted (1=yes, 2=no)? ")
    shift = int(input())
    # If the scores were shifted, request the shift amount
    if shift == 1:
        print("Shift amount? ")
        shift_amount = int(input())
        # Add the shift amount to the score
        score = score + shift_amount
        
        # If the score is greater than 100, restrict it to 100
        if score > 100:
            score = 100

    # Print the total points and calculate weighted score
    print("Total points = ", score, " / 100")
    print("Weighted score = ", round(score * weight / 100, 1), " / ", weight)
    print()

    # Return the weighted score
    return (score * weight / 100)

# Define the final_test function
def final_test():
    # Print the intro
    print("Final:")
    # Request the weight of the final
    print("Weight (0-100)? ")
    weight = int(input())
    # Request the score earned on the final
    print("Score earned? ")
    score = int(input())
    # Request if the scores were shifted
    print("Were scores shifted (1=yes, 2=no)? ")
    shift = int(input())
    # If the scores were shifted, request the shift amount
    if shift == 1:
        print("Shift amount? ")
        shift_amount = int(input())
        # Add the shift amount to the score
        score = score + shift_amount
        
        # If the score is greater than 100, restrict it to 100
        if score > 100:
            score = 100

    # Print the total points and calculate weighted score
    print("Total points = ", score, " / 100")
    print("Weighted score = ", round(score * weight / 100, 1), " / ", weight)
    print()

    # Return the weighted score
    return (score * weight / 100)

# Define the homework function
def homework():
    # Print the intro
    print("Homework:")
    # Request the weight of the homework
    print("Weight (0-100)? ")
    weight = int(input())
    # Request the number of assignments
    print("Number of assignments? ")
    num_assignments = int(input())
    # Initialize the total score and max points
    total_score = 0
    max_points = 0
    # Loop through the number of assignments
    for i in range(num_assignments):
        # Request the score earned on the assignment
        print("Assignment ", i+1, " score? ")
        score = int(input())
        # Request the max points on the assignment
        print("Assignment ", i+1, " max? ")
        max_score = int(input())
        # Add the score and max points to the total
        total_score = total_score + score
        max_points = max_points + max_score

    # Request how many sections were attended
    print("How many sections did you attend? ")
    num_sections = int(input())
    # Calculate the section points
    print('Section points = ', num_sections * 3, " / 34")
    # Simplify 
    total_points_with_sections = total_score + num_sections * 3
    # Print the total points and calculate weighted score
    print("Total points = ", total_points_with_sections, " / ", (max_points + 34))
    print("Weighted score = ", round((total_points_with_sections / (max_points + 34)) * weight, 1), " / ", weight)
    print()

    # Return the weighted score
    return ((total_points_with_sections / (max_points + 34)) * weight)

# Define the calculate_grade function
def calculate_grade(midterm_1_grade,midterm_2_grade,fina_test_grade,homework_grade):
    # Calculate the final grade
    final_grade = midterm_1_grade + midterm_2_grade + fina_test_grade + homework_grade

    # Print the final grade
    print("Overall percentage = ", round(final_grade, 1))

    # Determine the letter grade
    if (final_grade >= 90):
        print("Your grade will be at least: A")
        print("Genius??")
    elif (final_grade >= 80):
        print("Your grade will be at least: B")
        print("Good job!")
    elif (final_grade >= 70):
        print("Your grade will be at least: C")
        print("You can do better!")
    elif (final_grade >= 60):
        print("Your grade will be at least: D")
        print("You need to study more!")
    else:
        print("Your grade will be at least: F")
        print("You should drop out.")

# Call the main function 
main()