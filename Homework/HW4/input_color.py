# Write a piece of code that reads shorthand text description of a color and prints the longer equivalent. Acceptable color names are B for Blue, G for Green, and R for Red. If the user enters anything other than B, G, or R, print an error message. Here are some example interactions with your program: Make your program case-insensitive, so that it accepts lowercase letters as well as uppercase letters. Here are some example interactions with your program:
#
# What color do you want? B
# You have chosen Red.
#
# What color do you want? g
# You have chosen Green.
#
# What color do you want? X
# Unknown color: X

# Write your code here
color = input("What color do you want? ")
if color == "B" or color == "b":
    print("You have chosen Blue.")
elif color == "G" or color == "g":
    print("You have chosen Green.")
elif color == "R" or color == "r":
    print("You have chosen Red.")
else:
    print("Unknown color: " + color)
    