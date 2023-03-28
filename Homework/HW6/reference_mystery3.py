def mystery(x, a):
    a[x] += 1
    x += 1
    print(x, a)

def main():
    x = 1
    a = [0] * 2
    mystery(x, a)
    print(x, a)

    x -= 1
    a[1] = len(a)
    mystery(x, a)
    print(x, a)

main()