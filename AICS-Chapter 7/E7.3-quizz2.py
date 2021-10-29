def main():
    try:
        score = int(input('Enter quiz score: '))
        if 90 <= score <= 100:
            print('Grade of the score: A')
        elif 80 <= score < 90:
            print('Grade of the score: B')
        elif 70 <= score < 80:
            print('Grade of the score: C')
        elif 60 <= score < 70:
            print('Grade of the score: D')
        elif 0 <= score < 60:
            print('Grade of the score: F')
        else:
            print('Enter a valid score from 0 to 100')    
    except:
        print('Wrong input! Enter a valid score from 0 to 100')

main()