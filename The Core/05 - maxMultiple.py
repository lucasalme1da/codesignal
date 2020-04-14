def maxMultiple(divisor, bound):
    for i in range(bound, 0, -1):
        if (i % divisor == 0):
            return i