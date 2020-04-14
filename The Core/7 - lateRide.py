def lateRide(n):
    return sum(list(map(lambda y: int(y), list(str(n // 60) + str(round(n % 60))))))