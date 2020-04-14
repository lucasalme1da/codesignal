def buildPalindrome(st):
    st = list(st)
    prefix = []
    while (''.join(st) != ''.join(st[::-1])):
        prefix.append(st.pop(0))
    return ''.join(prefix + st + prefix[::-1])