def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum

def main():
    inFileName = input('Enter file name to open: ')
    inFile = open(inFileName, 'r')
    myList = inFile.readlines()
    toNumbers(myList)
    squareEach(myList)
    print(sumList(myList))
    inFile.close()

main()