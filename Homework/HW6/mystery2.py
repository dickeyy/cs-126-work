def list_mystery2(a):
    for i in range(1, len(a) - 1):
        a[i] = a[i - 1] - a[i] + a[i + 1]
    print(a)

a5 = [6, 0, -1, 3, 5, 0, -3]
list_mystery2(a5)