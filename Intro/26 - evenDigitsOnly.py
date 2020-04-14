def evenDigitsOnly(n):
    return all(map(lambda x: x % 2 == 0, list(map(int, str(n)))))