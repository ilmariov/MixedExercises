def main():
    weight = float(input('Enter weight in pounds: '))
    height = float(input('Enter height in inches: '))
    bmi = (weight * 720) / height**2
    if bmi < 19:
        print('Bellow the healthy range')
    elif bmi > 25:
        print('Above the healthy range')
    else:
        print('Within the healthy range')

main()