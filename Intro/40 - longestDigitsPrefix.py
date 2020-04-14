def longestDigitsPrefix(inputString):
    a = 0
    string = []
    for i in range(len(list(inputString))):
        if (inputString[i].isdigit()):
            while(inputString[i+a].isdigit()):
                string.append(inputString[i+a])
                a += 1
                if (i+a == len(inputString)):
                        return ''.join(string)
            return ''.join(string)
        else:
            return ''

