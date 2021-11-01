from graphics import *

def main():
    win = GraphWin('Bouncing ball', 640, 480)
    win.setCoords(0, 0, 100, 75)
    center = win.getMouse()
    ball = Circle(center, 8).draw(win)
    ball.setOutline('red')
    ball.setFill('red')
    dx, dy = 1, 1

    for i in range(500):
        ball.move(dx, dy)
        newCenter = ball.getCenter()
        x, y = newCenter.getX(), newCenter.getY()
        if x >= 100:
            dx = -1
        elif y >= 75:
            dy = -1
        elif x <= 0:
            dx = 1
        elif y <= 0:
            dy = 1
        update(30)

    message = Text(Point(50, 36), 'The End').draw(win)
    message.setSize(24)
    message.setStyle('bold')
    message.setTextColor('red')
    win.getMouse()
    win.close()

main()