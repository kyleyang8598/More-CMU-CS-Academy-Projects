# Kyle Yang
# Instructions: Press left, right, up, or down to move the boat
# Local Variables: Lines 30-40
# For Loops: Lines 33 and 80

from cmu_graphics import *

# Background
app.background = 'lightGreen'

# Lake
Rect(0,300,400,100,fill='aqua')

# Sidewalk
Rect(0,260,400,30,fill='gold')

# Road
road = Group(Rect(0,150,400,100),
            Line(0,200,400,200,fill='yellow',dashes=True))

# Boat
boat = Group(Polygon(150,350,250,350,225,375,175,375,fill='brown'),
            Polygon(200,300,225,330,200,330,fill='yellow'),
            Line(200,300,200,350,fill='saddleBrown',lineWidth=5))

boat.dx = 5
boat.dy = 5

# Stickman
stickmen = Group()

def createStickmen():
    newStickmanX = 100
    newStickmanSpeed = 1
    for i in range(5):
        stickman = Group(Circle(newStickmanX,235,10,fill='white',border='brown'),
                Line(newStickmanX,245,newStickmanX,265,fill='brown'),
                Line(newStickmanX-10,255,newStickmanX+10,255,fill='brown'),
                Line(newStickmanX,265,newStickmanX-10,275,fill='brown'),
                Line(newStickmanX,265,newStickmanX+10,275,fill='brown'))
        stickman.dx = newStickmanSpeed
        stickmen.add(stickman)
        newStickmanX += 50
        newStickmanSpeed += 1
createStickmen()

# Traffic Light
redLight = Circle(365,35,20,fill='darkRed')
greenLight = Circle(365,85,20,fill='lime')
trafficLight = Group(Rect(340,10,50,100,fill='gray'),redLight,greenLight)
trafficLight.time = 0

# Car
car = Group(Polygon(25,125,75,75,125,75,175,125,fill='blue'),
            Rect(25,125,200,50,fill='orange'),
            Rect(75,80,50,40),
            Circle(75,175,25,fill='lightGray',border='gray',borderWidth=10),
            Circle(175,175,25,fill='lightGray',border='gray',borderWidth=10))

car.dx = 10

# onStep
def onStep():
    if trafficLight.time == 100:
        if redLight.fill == 'red':
            greenLight.fill = 'lime'
            redLight.fill = 'darkRed'
        else:
            greenLight.fill = 'darkGreen'
            redLight.fill = 'red'
        trafficLight.time = 0
    if not car.centerX == 200 or not redLight.fill == 'red':
        if car.left > 400:
            car.right = 0
        else:
            if car.dx < 10:
                car.dx += 1
            car.centerX += car.dx
    else:
        car.dx = 0
    trafficLight.time += 1
    for stickman in stickmen:
        if stickman.left < 0 or stickman.right > 400:
            stickman.dx = -stickman.dx
        stickman.centerX += stickman.dx

# onKeyHold
def onKeyHold(keys):
    if 'left' in keys:
        if boat.left > 0:
            boat.centerX -= boat.dx
    if 'right' in keys:
        if boat.right < 400:
            boat.centerX += boat.dx
    if 'up' in keys:
        if boat.top > 300:
            boat.centerY -= boat.dy
    if 'down' in keys:
        if boat.bottom < 400:
            boat.centerY += boat.dy

# River Falls: Main Street 2


cmu_graphics.run()
