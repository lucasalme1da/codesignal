def shapeArea(n):
    a = 0
    for i in range(n):
        if (i == 0):
            a = 1
        a += (4 * i)
    return a