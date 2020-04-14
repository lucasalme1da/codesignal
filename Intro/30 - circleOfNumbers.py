def circleOfNumbers(n, firstNumber):
    firstHalf = []
    secondHalf = []
    for i in range(round(((n - 1)/2) + 0.5)):
        firstHalf.append(i)
        if (i == firstNumber):
            return i + round(((n - 1)/2) + 0.5)
    for j in range(round(((n - 1)/2) + 0.5), n):
        secondHalf.append(j)
        if (j == firstNumber):
            return j - round(((n - 1)/2) + 0.5)