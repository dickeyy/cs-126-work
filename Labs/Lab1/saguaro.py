# This program prints a saguaro cactus

# TODO: Make it actually dynamic for any number > 1

# Define the scale of the cactus (2-4)
SCALE = 3

# The main function prints the cactus
def main():
    if (SCALE >= 1):
        cactus_top()
        cactus_middle()
        cactus_bottom()
    else:
        print("The scale needs to be >= 1")

# Top of the cactus
def cactus_top():

    print(" ", "x"* SCALE, " " * (SCALE + 1), "x" * (SCALE * 2), sep="")

    for i in range(0, SCALE + (SCALE - 1)):
        x = (SCALE + (SCALE - 1))-i
        slash = "/" * i
        dash = "-" * x
    
        print("X", "-" * SCALE,  "X", " " * (SCALE -1), "X/", slash, dash, "X", sep="")
    
    print(" ", "x" * (SCALE * 2) , "X", "~" * (SCALE * 2), "X", " " * (SCALE), "x" * (SCALE), sep="")

# Middle of the cactus
def cactus_middle():

    space = (SCALE * 2) + 1
    for i in range(0,(SCALE * 2) -1):
        x = (SCALE + SCALE)-i
        dash = "-" * (x -1)
        slash = "\\" * i 
    
        print(" " * space,"X", dash, slash, "\\X", " " * (SCALE - 1) , "X", "-" * SCALE ,"X", sep="")
        
    print(" " * space,"X", "~" * (SCALE * 2), "X", "x" * (SCALE * 2), sep="")

    
# Bottom of the cactus
def cactus_bottom():

    space = (SCALE * 2) + 1
    for i in range(0,(SCALE * 2)):
        print(" " * space, "X", "~" * (SCALE * 2), "X", sep="")

main()