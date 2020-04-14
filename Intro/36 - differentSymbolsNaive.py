def differentSymbolsNaive(s):
    diffArray = []
    for i in range(len(list(s))):
        if list(s)[i] not in diffArray:
            diffArray.append(list(s)[i])
    return len(diffArray)