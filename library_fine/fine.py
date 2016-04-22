
# Library Fine
# https://www.hackerrank.com/challenges/library-fine


from datetime import date


def calculate(expected_date, actual_date):
    if actual_date <= expected_date:
        return 0

    if actual_date.year != expected_date.year:
        return 10000
    elif actual_date.month != expected_date.month:
        return 500 * (actual_date.month - expected_date.month)
    else:
        return 15 * (actual_date.day - expected_date.day)


if __name__ == "__main__":
    d1, m1, y1 = map(int, raw_input().strip().split())
    actual_date = date(year=y1, month=m1, day=d1)
    d2, m2, y2 = map(int, raw_input().strip().split())
    expected_date = date(year=y2, month=m2, day=d2)

    print calculate(expected_date, actual_date)
