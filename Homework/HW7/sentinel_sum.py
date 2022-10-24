total = 0 

def sentinel_sum():
    global total

    value = int(input("Type a number: "))

    if value == -1:
        print(f'Sum is {total}')
    else:
        
        total += value
        sentinel_sum()

sentinel_sum()