def message(level):
    print('Student classified as', level)

def main():
    try:
        earnedCredits = int(input('Enter credits earned: '))
        if 1 <= earnedCredits < 7:
            message('Freshman')
        elif 7 <= earnedCredits < 16:
            message('Sophomore')
        elif 16 <= earnedCredits < 26:
            message('Junior')
        elif 26 <= earnedCredits:
            message('Senior')
        else:
            print('Enter valid amount of credits')
    except:
        print('Enter only valid integers from 1')

main()