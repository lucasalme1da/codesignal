def isInfiniteProcess(a, b):
    return bool(b - a == 1 or a > b or (b-a) % 2 != 0)