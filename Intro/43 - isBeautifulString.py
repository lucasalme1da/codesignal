def isBeautifulString(inputString):
    sortedList = sorted(list(inputString))
    numberOfCharList = []
    counter = 0

    # Completing list with absent chars represented by 1
    sortedList = list(sum(zip(sortedList, sortedList), ()))
    first = 97
    for i in range(26):
        if (chr(first + i) not in sortedList):
            sortedList.append(chr(first + i))
    sortedList = sorted(sortedList)

    i = len(sortedList) - 1
    while(len(sortedList) > 0):
        current = sortedList[i]
        while(current in sortedList):
            counter += 1
            sortedList.remove(current)
        i -= counter
        numberOfCharList.append(counter)
        counter = 0
    numberOfCharList = numberOfCharList[::-1]

    for j in range(len(numberOfCharList) - 1):
        if (numberOfCharList[j] < numberOfCharList[j + 1]):
            return False
    return True