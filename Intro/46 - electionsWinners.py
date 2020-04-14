def electionsWinners(votes, k):
    m = max(votes)
    n = len(list(filter(lambda y: y, (map(lambda x: (x + k) > m, votes)))))
    votes.remove(max(votes))
    if n == 0 and m > max(votes):
        return 1
    return n