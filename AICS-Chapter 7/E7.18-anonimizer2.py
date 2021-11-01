from graphics import *
import math

def distance(p1,p2):
    dist = math.sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)
    return dist

def drawFace(center, radius, win):
    head = Circle(center, radius).draw(win)
    head.setOutline('orange')
    head.setFill('yellow')
    xCenter, yCenter = center.getX(), center.getY()
    eyeCenter = Point((xCenter - radius/4), (yCenter + radius/3))
    eyeRadius = radius/10
    eye1 = Circle(eyeCenter, eyeRadius).draw(win)
    eye1.setFill('brown')
    eye2 = eye1.clone()
    eye2.move((2*radius/4), 0)
    eye2.draw(win)

    initialX = int(-radius/2)
    finalX = int(radius/2)    
    for i in range(initialX, finalX+1):
        smileY = yCenter - math.sqrt((radius/2)**2 - i**2)
        smileX = i + xCenter
        mouthPoint = Circle(Point(smileX, smileY),1).draw(win)
        mouthPoint.setFill('brown')

def openPicture():
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
    window.setCoords(0, 0, widthPic, heightPic+30)
    placedPic.draw(window)
    win.close()

    return window, widthPic, heightPic

def main():
    try:
        win, x, y = openPicture()
        message1 = 'Enter the number of faces to be blocked, then click on window:'
        instruction1 = Text(Point(x/2, y+15), message1).draw(win)
        numOfFaces = Entry(Point(x-40, y+15), 2).draw(win)
        win.getMouse()
        n = numOfFaces.getText()
        instruction1.undraw()
        numOfFaces.undraw()
        message2 = 'Click on center and edge for each of the ' + n + ' faces to be drawn'
        instruction2 = Text(Point(x/2, y+15), message2).draw(win)

        for i in range(int(n)):
            center = win.getMouse()
            edge = win.getMouse()
            radius = distance(center, edge)
            drawFace(center, radius, win)

        instruction2.undraw()
        finalmsg = Text(Point(x/2, y+15), 'Done').draw(win)
        finalmsg.setSize(16)
        finalmsg.setStyle('bold')
        win.getMouse()
        win.close()

    except ValueError:
        print('Enter a valid positive integer')

    except:
        print ('File not in this folder')

main()