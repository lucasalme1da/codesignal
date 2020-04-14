def matrixElementsSum(matrix):
    sum = 0
    for l in range(len(matrix[0])):
        for c in range(len(matrix)):
            if (matrix[c][l] != 0):
                sum += matrix[c][l]
            else:
                break
    return sum
