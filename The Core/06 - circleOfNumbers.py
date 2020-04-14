def circleOfNumbers(n, firstNumber):
    nlist = list(range(0, n))
    if firstNumber < n/2:
        return nlist[int(n/2):][nlist.index(firstNumber)]
    return nlist[:int(n/2)][nlist.index(firstNumber) - int(n/2)]