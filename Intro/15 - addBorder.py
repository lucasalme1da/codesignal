def addBorder(picture):
    pictureWithBorder = []
    pictureWithBorder.append('*'*(len(picture[0])+2))
    for i in range(len(picture)):
        pictureWithBorder.append('*' + picture[i] + '*')
    pictureWithBorder.append('*'*(len(picture[0])+2))
    return pictureWithBorder