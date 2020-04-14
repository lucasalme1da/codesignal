def boxBlur(image):
    answer = []
    for i in range(len(image) - 2):
        rowAnswer = []
        for j in range(len(image[0]) - 2):
            rowAnswer.append(int(sum([image[i][j], image[i][j+1], image[i][j+2],
                                      image[i+1][j], image[i +
                                                           1][j+1], image[i+1][j+2],
                                      image[i+2][j], image[i+2][j+1], image[i+2][j+2]])/9))
        answer.append(rowAnswer)
    return answer
