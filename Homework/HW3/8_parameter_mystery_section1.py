# The following console program uses parameters and produces three lines of output. What are they?
def m(c, a, b):
    print(b, "+", c, "=", a)

def main():
    a = 4
    b = 7
    c = -2

    m(a, b, c)
    m(c, 3, a)
    m(a + b, b + c, c + a)

main()