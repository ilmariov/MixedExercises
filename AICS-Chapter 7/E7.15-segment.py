from graphics import *
import math

def main():
    win = GraphWin('Line Segment', 400, 400)
    win.setCoords(0, 0, 100, 100)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1, x2, y1, y2 = p1.getX(), p2.getX(), p1.getY(), p2.getY()
    seg = Line(Point(x1, y1), Point(x2, y2)).draw(win)
    dx, dy = (x2 - x1), (y2 - y1)
    mid_point = Circle(Point((x1 + (dx / 2)), (y1 + (dy / 2))), 1).draw(win)
    mid_point.setFill('red')
    length = math.sqrt(dx**2 + dy**2)
    Text(Point(85, 90), "Length: {0:0.2f}".format(length)).draw(win)

    if dx != 0:
        slope = dy / dx
        Text(Point(85, 75), "Slope: {0:0.2f}".format(slope)).draw(win)
    else:
        Text(Point(85, 75), "Slope: undetermined").draw(win)

    win.getMouse()
    win.close()

main()