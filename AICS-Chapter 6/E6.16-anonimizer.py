from graphics import *
import math

def square(x):
    return x**2

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX()-p1.getX()) + square(p2.getY()-p1.getY()))
    return dist

def drawFace(center, radius, win):
    head = Circle(center, radius)
    head.setOutline('orange')
    head.setFill('yellow')
    head.draw(win)
    xCenter = center.getX()
    yCenter = center.getY()
    eyeCenter = Point((xCenter - radius/4), (yCenter + radius/3))
    eyeRadius = radius/10
    eye1 = Circle(eyeCenter, eyeRadius)
    eye1.setFill('brown')
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move((2*radius/4), 0)
    eye2.draw(win)

    initialX = int(-radius/2)
    finalX = int(radius/2)
    for i in range(initialX, finalX+1):
        smileY = yCenter - math.sqrt(square(radius/2)-square(i))
        smileX = i + xCenter
        mouthPoint = Circle(Point(smileX, smileY),1)
        mouthPoint.setFill('brown')
        mouthPoint.draw(win)

def main():
    win = GraphWin('Anonimizer', 400, 100)
    Text(Point(200,35), 'Enter image filename, then click:').draw(win)
    picName = Entry(Point(200,75), 10)
    picName.setText('.PPM')
    picName.draw(win)
    win.getMouse()

    filename = picName.getText()
    picture = Image(Point(100, 100), filename)
    heightPic = picture.getHeight()
    widthPic = picture.getWidth()
    placedPic = Image(Point(widthPic/2, heightPic/2), filename)

    window = GraphWin('Anonimizer', widthPic, heightPic+30)
    placedPic.draw(window)
    win.close()

    window.setCoords(0, 0, widthPic, heightPic+30)
    instruction = Text(Point(widthPic/2, heightPic+15), 'Enter the number of faces to be blocked, then click on window:')
    instruction.draw(window)
    numOfFaces = Entry(Point(widthPic-40, heightPic+15), 2)
    numOfFaces.draw(window)
    window.getMouse()
    n = numOfFaces.getText()
    instruction.undraw()
    numOfFaces.undraw()
    message = 'Click on center and edge for each of the ' + n + ' faces to be drawn'
    Text(Point(widthPic/2, heightPic+15), message).draw(window)

    for i in range(int(n)):
        center = window.getMouse()
        edge = window.getMouse()
        radius = distance(center, edge)
        drawFace(center, radius, window)

    window.getMouse()
    window.close()
    
main()