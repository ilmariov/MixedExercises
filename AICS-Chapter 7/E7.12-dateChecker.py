def main():
    try:
        date = input('Enter date in numbers (mm/dd/year): ').split('/')
        month, day= int(date[0]), int(date[1])
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 1 <= month <= 12 and 1 <= day <= daysPerMonth[month - 1]:
            print('Valid date!')
        else:
            print('Sorry! Enter a valid date')
    except:
        print('Wrong input! Enter date in a valid format (mm/dd/year)')

main()