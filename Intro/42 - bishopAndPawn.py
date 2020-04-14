def bishopAndPawn(bishop, pawn):
    # Drawing the board
    board = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
             ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
             ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
             ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
             ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
             ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
             ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
             ['a1', 'a2', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]
    # Checking bishop possible movements
    posMov = []
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if (board[i][j] == bishop):
                # Moving topLeft
                a, b = i, j
                while(a != 0 and b != 0):
                    a -= 1
                    b -= 1
                    posMov.append(board[a][b])

                # Moving botLeft
                a, b = i, j
                while(a != len(board[0]) - 1 and b != 0):
                    a += 1
                    b -= 1
                    posMov.append(board[a][b])

                # Moving topRight
                a, b = i, j
                while(a != 0 and b != len(board[0]) - 1):
                    a -= 1
                    b += 1
                    posMov.append(board[a][b])

                # Moving botRight
                a, b = i, j
                while(a != len(board[0]) - 1 and b != len(board[0]) - 1):
                    a += 1
                    b += 1
                    posMov.append(board[a][b])
    # So we just have to check if the pawn position is in posMov and return the result
    return pawn in posMov