import math

def nextGuess(guess, x):
    nextGuess = (guess + x/guess) / 2
    return nextGuess

def main():
    x = float(input("Enter the value to find the square root: "))
    times = int(input("How many times you want to improve the guess: "))
    guess = x / 2

    for i in range(times):
        guess = nextGuess(guess, x)

    print('The final value of guess is:', guess)

    diff = math.sqrt(x) - guess
    print("The difference between the actual square root of x and the guess is:", diff)

main()