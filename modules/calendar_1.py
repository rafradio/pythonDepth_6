DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yearCheck = lambda y: 1 <= y <= 9999
monthCheck = lambda m: 1 <= m <= 12
dayCheck = lambda d, days: 1 <= d <= days

def isLeapYear(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def parseDate(data: str):
    return list(map(int, data.split('.')))

def checkData(data: str):
    day, month, year = parseDate(data)
    if not (yearCheck(year) and monthCheck(month)): return False

    days = DAYS_LEAP if isLeapYear(year) else DAYS

    if dayCheck(day, days[month-1]): return True
    return False

def takeData() -> str:
    return input("Введите дату: ")

__all__ = ['checkData', 'takeData']

