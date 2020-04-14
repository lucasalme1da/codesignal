def isIPv4Address(inputString):
    a = list(map(lambda x: x.isdigit() and int(x) >= 0 and int(x) <= 255, inputString.split('.')))
    if len(a) == 4:
        return all(list(map(lambda x: x.isdigit() and int(x) >= 0 and int(x) <= 255, inputString.split('.'))))
    return False