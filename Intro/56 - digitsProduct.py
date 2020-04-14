def digitsProduct(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1
    
    n = []

    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1

    return int(''.join(map(str, sorted(n))))