def arrayChange(inputArray):
    changes = 0
    for i in range(len(inputArray) - 1):
        # print(inputArray[i+1], inputArray[i])
        if (inputArray[i] >= inputArray[i+1]):
            aux = inputArray[i+1]
            inputArray[i+1] = inputArray[i] + 1
            changes += abs(aux - inputArray[i+1])
    # print('array -> ', inputArray)
    return changes