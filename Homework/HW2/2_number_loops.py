list = [1, 2, 3, 4, 5]
x = 4

for i in range(0, len(list)):

    print('.' * x, list[i] , '.' * i, sep="")

    x -= 1