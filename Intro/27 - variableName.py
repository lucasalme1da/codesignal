def variableName(name):
    permittedAlphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    if (list(name)[0].isdigit() or (not all(map(lambda x: x in permittedAlphabet, list(name))))):
        return False
    return True
