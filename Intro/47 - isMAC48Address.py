def isMAC48Address(inputString):
    return bool(re.search(
        r"\A[A-F\d][A-F\d]-[A-F\d][A-F\d]-[A-F\d][A-F\d]-[A-F\d][A-F\d]-[A-F\d][A-F\d]-[A-F\d][A-F\d]$", inputString))
