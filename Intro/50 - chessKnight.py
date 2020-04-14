def chessKnight(cell):
    if(bool(re.search("^[a|h][1|8]$", cell))):
        return 2
    if(bool(re.search("^[a|h][2|7]|[b|g][1|8]$", cell))):
        return 3
    if(bool(re.search("^[a|h][3-6]|[c|d|e|f][1|8]|[b|g][2|7]$", cell))):
        return 4
    if(bool(re.search("^[c|d|e|f][2|7]|[b|g][3-6]$", cell))):
        return 6
    return 8