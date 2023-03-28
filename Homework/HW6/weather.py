# Write a console program that reads an input file of temperatures, with numbers representing daily high temperatures such as:

# 16.2   23.2
#    19.2 7.7  22.9

# 18.4  -1.6 14.6
# Your program should prompt for the file name to read, then read its data and print the change in temperature between each pair of neighboring days.

# Input file? weather.txt 
# 16.2 to 23.2, change = 7.0
# 23.2 to 19.2, change = -4.0
# 19.2 to 7.7, change = -11.5
# 7.7 to 22.9, change = 15.2
# 22.9 to 18.4, change = -4.5
# 18.4 to -1.6, change = -20.0
# -1.6 to 14.6, change = 16.2
# If there are any non-numeric tokens of input in the file, your program should skip over them and ignore them. You may assume that the user types the name of a file that exists and is readable.

# Write your program here
def main():
    filename = input("Input file? ")
    file = open(filename, "r")
    for line in file:
        tokens = line.split()
        for i in range(len(tokens) - 1):
            print(tokens[i] + " to " + tokens[i + 1] + ", change = " + str(float(tokens[i + 1]) - float(tokens[i])))
    file.close()

main()

