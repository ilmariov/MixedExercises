def sumN(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range (1,n+1):
        cube = i ** 3
        sum = sum + cube
    return sum

def main():
    n = int(input('Enter a positive integer: '))
    natural = sumN(n)
    cubes = sumNCubes(n)
    print('The sum of the first {0} natural numbers is: {1}'. format(n, natural))
    print('The sum of the cubes of the first {0} natural numbers is: {1}'. format(n, cubes))

main()