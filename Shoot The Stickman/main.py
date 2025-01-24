# Kyle Yang
# Instructions: Shoot the stickman and get points with the cannon by clicking and aiming the mouse.
# randrange: Lines 42, 44, 46, and 48
# distance: Line 52
# angleTo: Line 60
# getPointInDir: Lines 50, 66, and 68

from cmu_graphics import *

# Background
app.background = 'skyBlue'

# Stickman
stickman = Group(Circle(200,200,10,fill='white',border='black'),
                Line(200,210,200,230),
                Line(190,220,210,220),
                Line(200,230,190,240),
                Line(200,230,210,240))

# Cannon
cannonBody = Group(Oval(20,200,50,30),
                Oval(40,200,10,30))

cannon = Group(Circle(10,220,10,fill='brown'),
                cannonBody)

# Cannon Ball
cannonBall = Circle(0,0,15,fill=gradient('white','black','black'),visible=False)

# Cannon Fire
cannonFire = Polygon(40,170,60,170,55,180,60,190,40,190,fill=gradient('yellow','red'),visible=False)

# Player Data
Label('Points:',180,10)
points = Label(0,220,10)
Label('Distance:',180,370)
Distance = Label(0,220,370)
Label('Angle:',180,390)
angle = Label(0,220,390)

# onStep
def onStep():
    if stickman.centerY >= 100:
        stickman.centerY -= randrange(10,30)
    if stickman.centerY < 300:
        stickman.centerY += randrange(10,30)
    if stickman.centerX >= 100:
        stickman.centerX -= randrange(10,30)
    if stickman.centerX < 300:
        stickman.centerX += randrange(10,30)
    if cannonBall.visible == True:
        cannonBall.centerX, cannonBall.centerY = getPointInDir(cannonBall.centerX,cannonBall.centerY,cannonFire.rotateAngle+90,10)
        if cannonBall.hitsShape(stickman):
            Distance.value = distance(cannonBody.centerX,cannonBody.centerY,stickman.centerX,stickman.centerY)//1
            stickman.centerX = randrange(100,300)
            stickman.centerY = randrange(100,300)
            cannonBall.visible = False
            points.value += 1

# onMouseMove
def onMouseMove(mouseX,mouseY):
    angle.value = angleTo(cannon.centerX,cannon.centerY,mouseX,mouseY)//1
    cannon.rotateAngle = angle.value - 90

# onMousePress
def onMousePress(mouseX,mouseY):
    cannonBall.visible = True
    cannonBall.centerX, cannonBall.centerY = getPointInDir(cannonBody.centerX,cannonBody.centerY,angle.value,30)
    cannonFire.visible = True
    cannonFire.centerX, cannonFire.centerY = getPointInDir(cannonBody.centerX,cannonBody.centerY,angle.value,30)
    cannonFire.rotateAngle = cannon.rotateAngle

# onMouseRelease
def onMouseRelease(mouseX,mouseY):
    cannonFire.visible = False

# Shoot The Stickman


cmu_graphics.run()
