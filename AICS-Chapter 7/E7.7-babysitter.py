def timeToNum(hours, minutes):
    numTime = hours + (minutes / 60)
    return numTime

def setTime(inputText):
    var = input(inputText).split(':')
    hh, mm = float(var[0]), float(var[1])
    time = timeToNum(hh, mm)
    return time

def main():
    try:
        start = setTime('Enter starting time (hh:mm) : ')
        end = setTime('Enter ending time (hh:mm) : ')
        if 6 <= end <= 21:
            bill = (end - start) * 2.5
            print('Total babysitting bill: $ {0:0.2f}'.format(bill))
        elif 21 < end <= 24:
            bill = (21-start)*2.5 + (end-21)*1.75
            print('Total babysitting bill: $ {0:0.2f}'.format(bill))
        else:
            print('Time off! Enter a valid hourly range')
    except:
        print('Wrong input! Sorry, try again.')

main()