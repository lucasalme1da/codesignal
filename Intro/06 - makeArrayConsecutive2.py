def makeArrayConsecutive2(statues):
    array = []
    for i in range(max(statues) + 1):
        if (i not in statues) and i > min(statues):
            array.append(i) 
    return len(array)
    
