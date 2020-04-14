def extractEachKth(inputArray, k):
    for i in range(k - 1, len(inputArray), k):
        print(i)
        if (i != 0 or k == 1):
            inputArray[i] = -21
    return list(filter(lambda x: x != -21, inputArray))