def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if (yourLeft == friendsLeft and yourRight == friendsRight):
        return True
    elif (yourLeft == friendsRight and friendsLeft == yourRight):
        return True
    return False