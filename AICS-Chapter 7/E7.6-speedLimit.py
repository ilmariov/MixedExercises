def main():
    sLimit = int(input('Enter speed limit: '))
    clockedSpeed = float(input('Enter clocked speed: '))
    dSpeed = clockedSpeed - sLimit
    if dSpeed <= 0:
        print('Legal speed')
    else:
        if clockedSpeed <= 90:
            fine = 50 + (dSpeed*5)
            print('Fine:', fine)
        else:
            fine = 50 + (90 - sLimit) * 5 + 200
            print('Fine:', fine)

main()