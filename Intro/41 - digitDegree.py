def digitDegree(n):
    array = list(map(lambda x: int(x), list(str(n))))
    if (len(array) == 1):
        return 0
    steps = 1
    while(sum(array) not in range(10)):
        aux = sum(array)
        array = (list(map(lambda x: int(x), list(str(aux)))))
        steps += 1
    return steps