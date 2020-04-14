def minesweeper(matrix):
    raw = []
    array = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            aux = 0

            # Corner
            if (row == 0 and col == 0):  # topLeftCorner
                if(matrix[row + 1][col]):
                    aux += 1
                if(matrix[row][col + 1]):
                    aux += 1
                if(matrix[row + 1][col + 1]):
                    aux += 1
                array.append(aux)
                continue
            if (row == 0 and col == (len(matrix[0]) - 1)):  # topRightCorner
                if(matrix[row + 1][col]):
                    aux += 1
                if(matrix[row][col - 1]):
                    aux += 1
                if(matrix[row + 1][col - 1]):
                    aux += 1
                array.append(aux)
                continue
            if ((row == len(matrix) - 1) and col == 0):  # bottomLeftCorner
                if(matrix[row - 1][col]):
                    aux += 1
                if(matrix[row][col + 1]):
                    aux += 1
                if(matrix[row - 1][col + 1]):
                    aux += 1
                array.append(aux)
                continue
            if ((row == len(matrix) - 1) and (col == len(matrix[0]) - 1)):
                if(matrix[row - 1][col]):
                    aux += 1
                if(matrix[row][col - 1]):
                    aux += 1
                if(matrix[row - 1][col - 1]):
                    aux += 1
                array.append(aux)
                continue

            # Sides
            if (col == 0):  # verticalLeft
                if(matrix[row - 1][col]):
                    aux += 1
                if(matrix[row - 1][col + 1]):
                    aux += 1
                if(matrix[row][col + 1]):
                    aux += 1
                if(matrix[row + 1][col + 1]):
                    aux += 1
                if(matrix[row + 1][col]):
                    aux += 1
                array.append(aux)
                continue
            if (col == len(matrix[0]) - 1):  # verticalRight
                if(matrix[row - 1][col]):
                    aux += 1
                if(matrix[row - 1][col - 1]):
                    aux += 1
                if(matrix[row][col - 1]):
                    aux += 1
                if(matrix[row + 1][col - 1]):
                    aux += 1
                if(matrix[row + 1][col]):
                    aux += 1
                array.append(aux)
                continue
            if (row == 0):  # horizontalTop
                if(matrix[row + 1][col]):
                    aux += 1
                if(matrix[row + 1][col - 1]):
                    aux += 1
                if(matrix[row + 1][col + 1]):
                    aux += 1
                if(matrix[row][col - 1]):
                    aux += 1
                if(matrix[row][col + 1]):
                    aux += 1
                array.append(aux)
                continue
            if (row == len(matrix) - 1):  # horizontalBottom
                if(matrix[row - 1][col]):
                    aux += 1
                if(matrix[row - 1][col - 1]):
                    aux += 1
                if(matrix[row - 1][col + 1]):
                    aux += 1
                if(matrix[row][col - 1]):
                    aux += 1
                if(matrix[row][col + 1]):
                    aux += 1
                array.append(aux)
                continue

            # Middle
            if(matrix[row - 1][col - 1]):
                aux += 1
            if(matrix[row - 1][col]):
                aux += 1
            if(matrix[row - 1][col + 1]):
                aux += 1
            if(matrix[row][col - 1]):
                aux += 1
            if(matrix[row][col + 1]):
                aux += 1
            if(matrix[row + 1][col - 1]):
                aux += 1
            if(matrix[row + 1][col]):
                aux += 1
            if(matrix[row + 1][col + 1]):
                aux += 1

            array.append(aux)

        raw.append(array)
        array = []
    return raw
