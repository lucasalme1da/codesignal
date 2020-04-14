def arrayMaxConsecutiveSum(inputArray, k):
    maximal = []
    maximal.append(sum(inputArray[:k]))
    for i in range(len(inputArray) - k):
        maximal.append(maximal[len(maximal) - 1] -
                       inputArray[i] + inputArray[k + i])
    return max(maximal)