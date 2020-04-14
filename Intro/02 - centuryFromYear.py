def centuryFromYear(year):
    if (year >= 1 and year <= 2005):
        if (year % 100 == 0):
            return year // 100
        else:
            return (year // 100) + 1
