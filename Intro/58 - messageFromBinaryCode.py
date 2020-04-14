def messageFromBinaryCode(code):
    result = []
    for i in range(0, len(code), 8):
        result.append(int(''.join(list(code)[0 + i:8 + i]), 2))
    return ''.join(list(map(lambda y: chr(int(y)), result)))