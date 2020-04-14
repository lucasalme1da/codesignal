def avoidObstacles(inputArray):
    if (0 not in inputArray):
        inputArray.append(0)
    inputArray = sorted(inputArray)
    for j in range(min(inputArray), max(inputArray)):
        if (j not in inputArray):
            inputArray.insert(j, -1)
    print(inputArray)

    # At this point, we have an array which the n'th element is equal to n - 1 and the gaps are filled with -1

    multiplier = 2
    pos = 1
    while((pos * multiplier) < len(inputArray)):
        print((pos * multiplier), inputArray[pos * multiplier])
        if(inputArray[pos * multiplier] != -1):
            pos = 1
            multiplier += 1
        else:
            pos += 1
    return multiplier