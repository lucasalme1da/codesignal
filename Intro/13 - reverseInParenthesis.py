def reverseInParentheses(inputString):
    i = 0
    while ('(' in inputString):
        i += 1
        if (inputString[i] == ')'):
            for j in range(i, -1, -1):
                if (inputString[j] == '('):
                    print(inputString[:j]+(inputString[j+1:i])
                          [::-1]+inputString[i+1:])
                    inputString = (inputString[:j]+(inputString[j+1:i])
                                   [::-1]+inputString[i+1:])
                    i = 0
                    break
    return inputString
	