# make a function called print_number_square that takes a max and min parameter. 
# and prints a square of lines of increasing numbers. the first lline should start with the minimum,
# and each line that follows should start with the next higher number. 
# the sequence of numbers on a line wraps back to the minumum after it hits the maximum

def print_number_square(min, max):
    for i in range(min, max + 1):
        for j in range(min, max + 1):
            print(i+j, end = "")
        print()
        

print_number_square(3, 7)