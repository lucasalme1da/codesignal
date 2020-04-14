def alphabeticShift(inputString):
    alphabet = 'zabcdefghijklmnopqrstuvwxyz'
    answer = []
    for i in range(len(list(inputString))):
        answer.append(alphabet[alphabet.index(
            list(inputString)[i]) + 1])
    return ''.join(answer)