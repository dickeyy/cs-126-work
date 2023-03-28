def orange(z, y, x):
    print(y, "and", z, "were", x)
    return x + y + z

def main():
    x = "happy"
    y = "pumpkin"
    z = "orange"
    pumpkin_str = "sleepy"
    orange_str = "vampire"

    orange(y, x, z)
    x = orange(x, z, y)
    orange(pumpkin_str, z, "y")
    z = "green"
    orange("x", "pumpkin", z)
    orange(x, z, orange_str)

main()