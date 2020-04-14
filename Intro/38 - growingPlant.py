def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = upSpeed
    while (height < desiredHeight):
        days += 1
        height += upSpeed - downSpeed
    return days
