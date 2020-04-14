def lineEncoding(s):
    s, ans, count = list(s), [], 0
    s.append('$')
    for i in range(len(s)-1):
        count += 1
        if(s[i+1] != s[i]):
            if (count != 1):
                ans.append(count)
            ans.append(s[i])
            count = 0
    return ''.join(map(str, ans))