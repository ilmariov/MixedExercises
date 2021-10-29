def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum

def main():
    n = int(input('How many numbers to sum?: '))
    nums = []
    for i in range(n):
        number = float(input('Enter number: '))
        nums.append(number)
    print(sumList(nums))

main()