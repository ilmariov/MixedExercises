from graphics import *
import math

def main():
    radius = float(input("Enter the radius of the circle: "))
    y = float(input("Enter the y-intercept of the line: "))

    win = GraphWin("Circle Intersection", 500, 440)
    win.setCoords(-10, -10, 15, 12)

    x_axis = Line(Point(-10, 0), Point(10.5, 0)).draw(win)
    x_axis.setWidth(2)
    y_axis = Line(Point(0, -10), Point(0, 10)).draw(win)
    y_axis.setWidth(2)

    circle = Circle(Point(0, 0), radius).draw(win)
    line = Line(Point(-10, y), Point(10, y)).draw(win)

    if abs(y) < radius:
        x1 = math.sqrt(radius**2 - y**2) * (-1)
        x2 = math.sqrt(radius**2 - y**2)

        p1 = Circle(Point(x1, y), 0.3).draw(win)
        p1.setFill("red")
        p2 = Circle(Point(x2, y), 0.3).draw(win)
        p2.setFill("red")

        Text(Point(0, 11), "The coordinates of the interception points are:").draw(win)
        Text(Point(12, 10), "P1 ({0:0.1f}, {1})".format(x1, y)).draw(win)
        Text(Point(12, 9), "P2 ({0:0.1f}, {1})".format(x2, y)).draw(win)

    elif abs(y) == radius:
        p1 = Circle(Point(0, y), 0.3).draw(win)
        p1.setFill("red")
        Text(Point(0, 11), "The coordinate of the interception point is:").draw(win)
        Text(Point(12, 11), "P1 (0, {0})".format(y)).draw(win)

    else:
        Text(Point(0, 11), "There's no interception point").draw(win)

    win.getMouse()
    win.close()

main()