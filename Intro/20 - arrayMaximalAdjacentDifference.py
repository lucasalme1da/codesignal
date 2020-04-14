def arrayMaximalAdjacentDifference(inputArray):
    maximal = 0
    for i in range(len(inputArray) - 1):
        result = abs(inputArray[i] - inputArray[i + 1])
        if (result > maximal):
            maximal = result
    return maximal