def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def main():
    n = int(input('How many numbers to square?: '))
    numbers = []
    for i in range(n):
        num = float(input('Enter number: '))
        numbers.append(num)
    squareEach(numbers)
    print(numbers)

main()