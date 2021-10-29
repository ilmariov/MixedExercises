def main():
    hours = int(input('How many hours worked? '))
    rate = int(input('Enter hourly rate: '))
    if hours <= 40:
        wage = hours * rate
    else:
        overtime = hours - 40
        wage = (40*rate) + (1.5 * overtime *rate)
    print('Total wage for the week is', wage)

if __name__ == '__main__':
    main()