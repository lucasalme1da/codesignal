def depositProfit(deposit, rate, threshold):
    counter = 0
    while(deposit < threshold):
        deposit += deposit * (rate/100)
        counter += 1
        print(deposit)
    return counter