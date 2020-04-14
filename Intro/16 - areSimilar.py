def areSimilar(a, b):
    if (a == b):
        return True
    a = [x/y for x, y in zip(a, b)]
    b = list(filter(lambda x: x != 1, a))
    return len(b) == 2 and (round(1/b[0],5) == round(b[1],5))