def sum_of_digits(num): 
    sum = 0

    # if the number is negative, drop the negative sign and add all th integers of the digit
    if num < 0:
        num = num * -1
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum

    else:
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum