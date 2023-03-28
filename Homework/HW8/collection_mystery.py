def collection_mystery1(map):
    result = {}
    for k in map.keys():
        v = map[k]
        if k[0] <= v[0]:
            result[k] = v
        else:
            result[v] = k
    print(result)

balls = {'cotton': 'shirt', 'tree': 'violin', 'seed': 'tree', 'light': 'tree', 'rain': 'cotton'}

collection_mystery1(balls)