def mystery(n):
    if n < 0:
        n = n * 3
        print(n)
    else:
        n = n + 3
        if n % 2 == 1:
            n = n + n % 10
        print(n)

mystery(-5)
mystery(0)
mystery(7)
mystery(18)
mystery(49)