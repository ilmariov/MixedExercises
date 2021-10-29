def acronym(phrase):
    ph_list = phrase.split()
    acronym = []
    for word in ph_list:
        word = word.upper()
        print(word[0], end='')

def main():
    phrase = input('Enter a phrase: ')
    print('The acronym is: ', end='')
    acronym(phrase)
    print()

main()