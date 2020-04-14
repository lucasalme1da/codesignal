def knapsackLight(value1, weight1, value2, weight2, maxW):
    opt1 = [value1, weight1]
    opt2 = [value2, weight2]
    if (opt1[1] + opt2[1] <= maxW):
        print(opt1[1], opt2[1], maxW)
        return opt1[0] + opt2[0]
    elif (opt1[1] > maxW and opt2[1] <= maxW):
        return opt2[0]
    elif (opt2[1] > maxW and opt1[1] <= maxW):
        return opt1[0]
    elif (opt1[1] > maxW and opt2[1] > maxW):
        return 0
    else:
        return max(opt1[0], opt2[0])