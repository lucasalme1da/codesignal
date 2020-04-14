def commonCharacterCount(s1, s2):
    a = []
    b = list(s2)
    for i in range(len(s1)):
        if (s1[i] in b):
            a.append(s1[i])
            b.remove(s1[i])
    return len(a)