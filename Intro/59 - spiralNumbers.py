def spiralNumbers(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    numbers = 1
    l = 0
    while (numbers <= n * n):

         # To Right
        for i in range(0 + l, n - l):
            matrix[l][i] = numbers
            numbers += 1

        # To Down
        for j in range(1 + l, n - l):
            matrix[j][n - 1 - l] = numbers
            numbers += 1

        # To Left
        for k in range(n - 2 - l, -1 + l, -1):
            matrix[n - 1 - l][k] = numbers
            numbers += 1

        # To Up
        for m in range(n - 2 - l, 0 + l, -1):
            matrix[m][l] = numbers
            numbers += 1

        l += 1
    return matrix
