def zune_bug(days):
    year = 1980
    while days > 365:   # subtract out years
        if is_leap_year(year):
            if days > 366:
                days -= 366
                year += 1
            else:
                break
        else:
            days -= 365
            year += 1
    print("days =", days, ", year =", year)

zune_bug(10000)