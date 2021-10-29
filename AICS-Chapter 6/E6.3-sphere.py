import math

def sphereArea(radius):
    area = 4 * math.pi * radius * radius
    return area

def sphereVolume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

def main ():
    radius = float(input("Enter the radius of the sphere in cm: "))
    area = sphereArea(radius)
    volume = sphereVolume(radius)
    print ("The volume of the sphere is {0:0.2f} cm3, and its area is {1:0.2f} cm2".format(volume, area))

main()