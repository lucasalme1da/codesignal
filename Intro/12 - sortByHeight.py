def sortByHeight(a):
    trees = []
    peoples = []
    for i in range(len(a)):
        if (a[i] != -1):
            peoples.append(a[i])
        else:
            trees.append(i)
    peoples = sorted(peoples)
    for i in range(len(trees)):
        peoples.insert(trees[i], -1)
    return peoples