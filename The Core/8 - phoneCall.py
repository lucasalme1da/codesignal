def phoneCall(min1, min2_10, min11, s):
    minutes = 0
    if (s >= min1):
        minutes = 1
        s -= min1
    for i in range(2, 11):
        if (s > min2_10):
            s -= min2_10
            minutes += 1
        else:
            return minutes
    while(s >= min11):
        s -= min11
        minutes += 1
    return minutes