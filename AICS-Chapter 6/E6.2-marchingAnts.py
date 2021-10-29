def intro(litNum):
    print ('The ants go marching {0} by {0}, hurrah! hurrah!'.format(litNum))
    print ('The ants go marching {0} by {0}, hurrah! hurrah!'.format(litNum))
    print ('The ants go marching {0} by {0},'.format(litNum))

def complement(phrase):
    print('The little one stops to ' + phrase + ',')
    print('And they all go marching down...')
    print('To the ground...')
    print('To get out...')
    print('Of the rain.')
    print('Boom! Boom! Boom!')

def main():
    literalNums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    activities = ['suck his thumb', 'tie his shoe', 'climb a tree', 'shut the door',
                'take a dive', 'pick up sticks', 'pray to heaven', 'roller skate',
                'check the time']

    for i in range(9):
        intro(literalNums[i])
        complement(activities[i])
        print()

    intro('ten')
    print('The little one stops to shout: "The End!"')


main()