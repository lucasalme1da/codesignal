def deleteDigit(n):
    n = list(str(n))
    numbers = []
    for j in range(len(n) - 1, 0, -1):
        for i in range(len(n)):
            numbers.append(''.join(n[:i]+n[i+1:]))
        n.pop(j)
    numbers = list(map(int, numbers))
    return max(numbers)