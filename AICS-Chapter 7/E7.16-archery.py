from graphics import *
import math

def distance(p1,p2):
    dist = math.sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)
    return dist

def drawArchery():
    win = GraphWin("Archery Target", 500, 540)
    center = Point(250, 290)
    white = Circle(center, 200).draw(win)
    black = Circle(center, 160).draw(win)
    black.setFill("black")
    blue = Circle(center, 120).draw(win)
    blue.setFill("blue")
    red = Circle(center, 80).draw(win)
    red.setFill("red")
    yellow = Circle(center, 40).draw(win)
    yellow.setFill("yellow")
    return win, center

def setLabel(win, score):
    label = Text(Point(250, 30), 'Score: {0}'.format(score)).draw(win)
    return label

def main():
    win, center = drawArchery()
    score = 0
    label = setLabel(win, score)
    
    for i in range(5):
        shot = win.getMouse()
        label.undraw()
        radius = distance(center, shot)
        if radius <= 40:
            score = score + 9
        elif 40 < radius <= 80:
            score = score + 7
        elif 80 < radius <= 120:
            score = score + 5
        elif 120 < radius <= 160:
            score = score + 3
        elif 160 < radius <= 200:
            score = score + 1
        label = setLabel(win, score)

    win.getMouse()
    win.close()

main()