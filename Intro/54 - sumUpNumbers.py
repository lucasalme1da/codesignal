def sumUpNumbers(inputString):
    return sum(list(map(int, re.findall("[0-9]+", inputString))))