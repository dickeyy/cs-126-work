# Write code to read an integer from the user, then print even if that number is an even number or odd otherwise. You may assume that the user types a valid integer. The input/output should match the following example:

# Type a number: 14
# even

# Write code
number = int(input("Type a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")