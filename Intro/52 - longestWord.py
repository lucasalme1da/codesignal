def longestWord(text):
    l = re.findall("[a-zA-Z]+", text)
    s = list(map(lambda y: len(list(y)), l))
    return l[s.index(max(s))]