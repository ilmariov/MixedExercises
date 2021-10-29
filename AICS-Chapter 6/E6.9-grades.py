def grades(score):
    grade = 'FFFFFFDCBAA'
    score = score//10
    return grade[score]

def main():
    score = int(input('Enter a score (0-100): '))
    grade = grades(score)
    print('The corresponding grade for {0} points is: {1}'.format(score, grade))

main()