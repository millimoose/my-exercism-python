def _is_leap_year(year) -> bool:
    by_4 = not year % 4
    not_by_100 = year % 100
    by_400 = not year % 400
    return bool(by_400 or (by_4 and not_by_100))

def __is_leap_year(year) -> bool:
    return not(year % 400 and (year % 4 or not year % 100))

def is_leap_year(year) -> bool:
    return not (year % 400) or not 