def absoluteValuesSumMinimization(a):
    search = (list(map(lambda x: sum(map(lambda y: abs(y - x), a)), a)))
    return a[search.index(min(search))]