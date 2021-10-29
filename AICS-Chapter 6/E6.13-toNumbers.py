def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def main():
    n = int(input('How many strings in the list?: '))
    toNumsList = []
    for i in range(n):
        strNum = input('Enter number as string: ')
        toNumsList.append(strNum)
    toNumbers(toNumsList)
    print(toNumsList)

main()