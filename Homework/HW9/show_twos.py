

# Write a function called show_twos that accepts an parameter x as an integer, then prints the number as a product of factors of 2 and an odd number. For example, show_twos(120) should print 2 * 2 * 2 * 15. You may assume that x is greater than 0.

# The idea is to express the number as a product of factors of 2 and an odd number. The number 120 has 3 factors of 2 multiplied by the odd number 15. For odd numbers (e.g. 7), there are no factors of 2, so you just show the number itself. Assume that your function is passed a number greater than 0.

# Write your function here:
def show_twos(x):
    print(f"{x} = ", end = "")
    if x % 2 == 0:
        print("2 * ", end="")
        show_twos(x // 2)
    else:
        print(x)

show_twos(68)