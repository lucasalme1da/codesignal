def palindromeRearranging(inputString):
    alphabet = [[], [], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], [], []]
    alphabetIndex = 0
    inputArray = list(inputString)
    if (len(inputArray) == 0):
        return False
    for i in range(26):
        print(inputArray)
        while(chr(97 + i) in inputArray):
            inputArray.remove(chr(97+i))
            alphabet[alphabetIndex].append(chr(97 + i))
        alphabetIndex += 1

        if (len(inputArray) == 0):
            break
    print(alphabet)
    odds = []
    for j in range(len(alphabet)):
        if (len(alphabet[j]) % 2 != 0 and alphabet[j] not in odds):
            odds.append(alphabet[j])
            if (len(odds) > 1):
                return False
    return True