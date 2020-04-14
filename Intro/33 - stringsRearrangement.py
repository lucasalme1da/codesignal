from itertools import permutations

def diff(w1, w2):
    return sum([x[0] != x[1] for x in zip(w1, w2)]) == 1

def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False
