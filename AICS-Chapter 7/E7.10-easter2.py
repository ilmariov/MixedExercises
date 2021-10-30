def easterDay(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    day = 22 + d + e
    return day

def printDate(year, month, day):
    print('Easter in {0} is in {1} {2}th'.format(year, month, day))

def main():
    try:
        year = int(input('Enter a year between 1900-2099: '))

        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            day = easterDay(year)
            day = day - 7
            if day <= 31:
                printDate(year, 'March', day)
            else:
                newDay = day - 31
                printDate(year, 'April', newDay)
        elif 1900 <= year <= 2099:
            day = easterDay(year)
            if day <= 31:
                printDate(year, 'March', day)
            else:
                newDay = day - 31
                printDate(year, 'April', newDay)
        else:
            print('Enter a valid year between 1900 and 2099.')
    except:
        print('Wrong input!')

main()