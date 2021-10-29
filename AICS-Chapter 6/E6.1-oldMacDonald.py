def chorus():
    print ('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')

def lyric(animal, sound):
    chorus()
    print ('And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!'.format(animal))
    print ('with a {0}, {0} here and a {0}, {0} there.'.format(sound))
    print ('Here a {0}, there a {0}, everywhere a {0}, {0}'.format(sound))
    chorus()

def main():
    lyric('cow', 'moo')
    print()
    lyric('pig', 'oink')
    print()
    lyric('dog', 'woof')
    print()
    lyric('duck', 'quack')
    print()
    lyric('chick', 'cheep')

main()