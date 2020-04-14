def differentSquares(matrix):
    answer = []
    for j in range(len(matrix) - 1):
        for i in range(len(matrix[0]) - 1):
            square = [matrix[j][i], matrix[j + 1]
                      [i], matrix[j][i + 1], matrix[j + 1][i + 1]]
            if square not in answer:
                answer.append(square)
    return len(answer)