import math

def pizzaArea(diameter):
    area = math.pi * (diameter / 2) ** 2
    return area

def costInCents(price, area):
    costPerSquareInch = (price / area) * 100
    return costPerSquareInch

def main():
    diameter = float(input("Enter the diameter of the pizza in inches: "))
    price = float(input("Enter the price of the pizza in dollars: "))
    print()
    area = pizzaArea(diameter)
    cost = costInCents(price, area)
    print("The pizza costs {0:0.1f} cents per square inch.".format(cost))

main()