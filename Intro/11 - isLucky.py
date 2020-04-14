def isLucky(n):
    array = list(map(int, str(n)))
    return sum(array[:int(len(array)/2)]) == sum(array[int(len(array)/2):])
