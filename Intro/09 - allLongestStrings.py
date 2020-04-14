def allLongestStrings(inputArray):
    longestString = 0
    for i in range(len(inputArray)):
        if (len(inputArray[i]) > longestString):
            longestString = len(inputArray[i])
    return list(filter(lambda x: len(x) == longestString, inputArray))