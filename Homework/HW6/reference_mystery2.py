def mystery(x, a):
    x = x * 2
    if x > 6:
        a[2] = 14
        a[1] = 9
    else:
        a[0] = 9
        a[3] = 14
    print(x, a)

def main():
    x = 1
    a = [0] * 4

    x = x * 2
    mystery(x, a)
    print(x, a)

    x = x * 2
    mystery(x, a)
    print(x, a)

main()