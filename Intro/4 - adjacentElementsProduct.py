def adjacentElementsProduct(inputArray):
    math = 0
    for i in range(len(inputArray) - 1):
        math = inputArray[i] * (inputArray[i + 1])
        if (i == 0):
            result = math
        print(inputArray[i], inputArray[i+1], math)
        if (math > result):
            result = math
    return result