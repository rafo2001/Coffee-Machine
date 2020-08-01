def isYearLeap(year):
    if year % 4 != 0: return False
    elif year % 100 != 0: return True
    elif year % 400 != 0: return False
    else: return True


def daysInMonth(year, month):
    diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return diasMes[month - 1]


def dayOfYear(year, month, day):
    dia_del_anio = 0
    for mes in range(1, month):
        dia_del_anio += daysInMonth(year, mes)
    dia_del_anio += day
    return dia_del_anio


print(dayOfYear(2001, 12, 31))
testYears = [2020, 2020, 2020, 2020, 2019]
testMonths = [1, 3, 12, 5, 12]
testDays = [31, 1, 31, 17, 31]
testResults = [31, 61, 366, 138, 365]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    dy = testDays[i]
    print(yr, mo, dy, "-> ", end="")
    result = dayOfYear(yr, mo, dy)
    print(result, end="")
    if result == testResults[i]:
        print(" OK")
    else:
        print(" Failed")
