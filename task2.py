import calendar


def calendar_year(year):
    return calendar.calendar(year)


def calendar_month(year, month):
    return calendar.month(year, month)


if __name__ == "__main__":
    print(calendar_year(2024))
    print(calendar_month(2024, 7))
