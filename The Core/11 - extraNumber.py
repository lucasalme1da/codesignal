def extraNumber(a, b, c):
    l = [a, b, c]
    for i in range(3):
        aux = l[i]
        l.remove(aux)
        if aux not in l:
            return aux
        l.insert(i, aux)