# Write your function here:
def banish(a1, a2):
    if len(a2) == 0:
        return

    for i in range(len(a1)):
        if a1[i] in a2:
            for j in range(i, len(a1) - 1):
                a1[j] = a1[j + 1]
            a1[len(a1) - 1] = 0
