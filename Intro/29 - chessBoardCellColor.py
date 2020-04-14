def chessBoardCellColor(cell1, cell2):
    colors = []
    if ((ord(list(cell1)[0]) % 2) == (0 == ord(list(cell1)[1]) % 2 == 0)):
        colors.append(1)
    else:
        colors.append(0)

    if ((ord(list(cell2)[0]) % 2) == (0 == ord(list(cell2)[1]) % 2 == 0)):
        colors.append(1)
    else:
        colors.append(0)

    return colors[0] == colors[1]