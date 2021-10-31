def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dateChecker(month, day):
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12 and 1 <= day <= daysPerMonth[month - 1]:
        return True
    else:
        print('Sorry! Enter a valid date')
        return False

def main():
    try:
        date = input('Enter date in numbers (mm/dd/year): ').split('/')
        month, day, year = int(date[0]), int(date[1]), int(date[2])
        if dateChecker(month, day) == True:
            dayNum = 31 * (month - 1) + day
            if month > 2:
                dayNum = dayNum - ((4 * month + 23) // 10)
                if leap(year) == True:
                    dayNum = dayNum + 1
            print('It is day number', dayNum)
        
    except:
        print('Wrong input! Enter date in a valid format (mm/dd/year)')

main()