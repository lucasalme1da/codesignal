def reachNextLevel(experience, threshold, reward):
    return bool(experience + reward >= threshold)