def sudoku(grid):
    # Checking Lines
    if not all(list(map(lambda y: len(y) == len(set(y)), grid))):
        return False

    # Checking Columns
    columns = []
    for i in range(len(grid[0])):
        columns.append(list(map(lambda x: x[i], grid)))
    if not all(list(map(lambda y: len(y) == len(set(y)), columns))):
        return False

    # Checking sub-grids
    subGrids = []
    for j in range(0, 9, 3):
        for i in range(0, 9, 3):
            l1 = grid[0 + j][i:i + 3]
            l2 = grid[1 + j][i:i + 3]
            l3 = grid[2 + j][i:i + 3]
            subGrids.append(l1+l2+l3)
    if not all(list(map(lambda y: len(y) == len(set(y)), subGrids))):
        return False

    return True