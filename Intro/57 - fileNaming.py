def fileNaming(names):
    passed = []
    while(len(list(set(names))) != len(names)):
        for i in range(len(names)):
            repetitions = len(list(filter(lambda y: y == names[i], names)))
            if repetitions > 1:
                renameRepetitions(names, repetitions, passed, i)

            else:
                passed.append(names[i])
    return names


def renameRepetitions(names, repetitions, passedBefore, pos):
    oneTimeRepetition = 0
    repStart = 1
    j = pos
    passedAfter = []
    while (j < len(names)):
        if names[pos] == names[j]:
            predict = ''.join(names[j] + '(' + str(repStart) + ')')
            if predict not in passedAfter and predict not in passedBefore:
                if oneTimeRepetition > 0:
                    names[j] = predict
                    passedAfter.append(names[j])
                    j += 1
                    repStart += 1
                else:
                    oneTimeRepetition = 1
                    j += 1
            else:
                repStart += 1
        else:
            passedAfter.append(names[j])
            j += 1