def almostIncreasingSequence(handler):
    ignoredNumber = 0
    for i in range(len(handler) - 1):
        print(handler[i+1], handler[i])
        if (handler[i+1] <= handler[i] and ignoredNumber <= 1):
            ignoredNumber += 1
        elif(ignoredNumber == 1):
            if (handler[i+1] <= handler[i-1]):
                return False
        elif(ignoredNumber > 1):
            return False
    if (ignoredNumber <= 1):
        return True
    else:
        return False