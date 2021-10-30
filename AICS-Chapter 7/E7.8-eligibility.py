def main():
    try:
        age = int(input('Enter age: '))
        citizenTime = int(input('Enter years of citizenship: '))
        if age >= 30:
            if citizenTime >= 9:
                print('Eligible to be US Senator or US Representative')
            elif citizenTime >= 7:
                print('Eligible to be US Representative')
            else:
                print('Non eligible')
        elif age >= 25:
            if citizenTime >= 7:
                print('Eligible to be US Representative')
            else:
                print('Non eligible')
        else:
            print('Non eligible')
    except:
        print('Enter valid data')

main()