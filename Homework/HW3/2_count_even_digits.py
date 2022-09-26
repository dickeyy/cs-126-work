def count_even_digits(num=int, count=int):
    evens = 0
    numStr = str(num)
    numSplit = list(numStr)
    for i in range(count):
        if int(numSplit[i]) % 2 == 0:
            evens += 1

    return evens

print(count_even_digits(123456789, 9))