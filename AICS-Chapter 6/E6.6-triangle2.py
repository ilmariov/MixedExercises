import math
from graphics import *

def square(x):
    return x**2

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX()-p1.getX()) + square(p2.getY()-p1.getY()))
    return dist

def area(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    win = GraphWin('Draw a Triangle')
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 1.0), 'Click on three points')
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill('peachpuff')
    triangle.setOutline('cyan')
    triangle.draw(win)

    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    perim = a + b + c
    triangleArea = area(a,b,c)
    message.setText('The perimeter is: {0:0.2f}\nand the area: {1:0.2f}'.format(perim, triangleArea))

    win.getMouse()
    win.close()

main()