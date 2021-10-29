def main():
    try:
        score = int(input('Enter quiz score: '))
        if score == 5:
            print('Grade of the score: A')
        elif score == 4:
            print('Grade of the score: B')
        elif score == 3:
            print('Grade of the score: C')
        elif score == 2:
            print('Grade of the score: D')
        else:
            print('Grade of the score: F')
    except:
        print('Enter a valid score, integer from 0 to 5')

main()