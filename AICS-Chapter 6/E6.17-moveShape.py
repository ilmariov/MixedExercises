from graphics import *

def moveTo(shape, newCenter):
    currentCenter = shape.getCenter()
    dx = newCenter.getX() - currentCenter.getX()
    dy = newCenter.getY() - currentCenter.getY()
    return dx, dy

def main():
    win = GraphWin('Moving Shapes', 640, 480)    
    center = win.getMouse()
    circle = Circle(center, 50)
    circle.draw(win)

    for i in range(10):
        newCenter = win.getMouse()
        dx, dy = moveTo(circle, newCenter)
        circle.move(dx, dy)
    
    win.getMouse()
    win.close()

main()