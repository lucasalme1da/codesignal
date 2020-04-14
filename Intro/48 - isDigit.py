def isDigit(symbol):
    return bool(re.search("^\d$", str(symbol)))