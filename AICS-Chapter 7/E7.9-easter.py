def main():
    year = int(input('Enter a year between 1982-2048: '))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    day = 22 + d + e
    if day <= 31:
        print('Easter in {0} is in March {1}th'.format(year, day))
    else:
        newDay = day - 31
        print('Easter in {0} is in April {1}th'.format(year, newDay))
    
main()