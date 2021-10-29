from graphics import *
import math

def drawFace(center, size, win):
    faceRadius = 20*size
    head = Circle(center, faceRadius)
    head.draw(win)
    xCenter = center.getX()
    yCenter = center.getY()
    eyeCenter = Point((xCenter - faceRadius/4), (yCenter + faceRadius/3))
    eyeRadius = 2*size
    eye1 = Circle(eyeCenter, eyeRadius)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move((2*faceRadius/4), 0)
    eye2.draw(win)

    initialX = int(-faceRadius/2)
    finalX = int(faceRadius/2)
    for i in range(initialX, finalX+1):
        smileY = yCenter - math.sqrt((faceRadius/2)**2-(i**2))
        smileX = i + xCenter
        Point(smileX, smileY).draw(win)

def main():
    win = GraphWin('Drawing Faces', 500, 500)
    win.setCoords(0, 0, 500, 500)
    Text(Point(250, 485), '1. Enter number of faces you want to draw, then click: ').draw(win)
    facesQuantity = Entry(Point(460, 485), 3)
    facesQuantity.setText('0')
    facesQuantity.draw(win)
    Text(Point(250, 460), '2. Enter size then click to place center of the face: ').draw(win)
    inputSize = Entry(Point(460, 460), 3)
    inputSize.setText('0')
    inputSize.draw(win)

    win.getMouse()
    n = int(facesQuantity.getText())

    for i in range(n):
        center = win.getMouse()
        size = int(inputSize.getText())
        drawFace(center, size, win)
    
    win.getMouse()
    win.close()

main()
