def collection_mystery3(q):
    s = []
    size = len(q)
    for i in range(size):
        n = q.pop(0)
        if n % 2 == 0:
            s.append(n)
        else:
            q.append(n)
    print("q=" + str(q))
    print("s=" + str(s))

ass = [30, 20, 10, 60, 50, 40, 3, 0]	
collection_mystery3(ass)