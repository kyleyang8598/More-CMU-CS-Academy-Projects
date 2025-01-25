'''
Stormy weather continues to rock over a pile of traffic.
Instructions: Left click the mouse to initiate a lightning strike somewhere.
(You can only initiate a lightning strike when it's raining)
'''

from cmu_graphics import *

# Globals
app.background = 'lightBlue'
app.lightningRate = 0
app.stormDuration = 0
app.stormActivate = False
app.currentStrike = False

# Sun
sun = Oval(375,25,100,100,fill=gradient('yellow','orange'),border='lightYellow',borderWidth=1)

# Grass
grass = Rect(0,200,400,200,fill='lightGreen')

# Sidewalk
sidewalk = Rect(0,360,400,30,fill='gold')

# Road
road = Group(Rect(0,250,400,100),
            Line(0,300,400,300,fill='yellow',dashes=True))

# Traffic Light
redLight = Circle(365,135,20,fill='darkRed')
greenLight = Circle(365,185,20,fill='lime')
trafficLight = Group(Rect(340,110,50,100,fill='gray'),redLight,greenLight)
trafficLight.time = 0

# Car
car = Group(Polygon(25,225,75,175,125,175,175,225,fill='indigo'),
            Rect(25,225,200,50,fill='violet'),
            Rect(75,180,50,40),
            Circle(75,275,25,fill=gradient('lightGray','darkGray'),border='gray',borderWidth=10),
            Circle(175,275,25,fill=gradient('lightGray','darkGray'),border='gray',borderWidth=10))

car.dx = 10

# Clouds
cloud1 = Oval(50,25,150,50,fill='white')
cloud2 = Oval(150,25,150,50,fill='white')
cloud3 = Oval(250,25,150,50,fill='white')

# Rain
rain = Group()

# Lightning
lightning = Group()

def Clouds(length,width,color):
    # Changes clouds' color and size
    cloud1.width=width
    cloud1.length=length
    cloud1.fill=color
    cloud2.width=width
    cloud2.length=length
    cloud2.fill=color
    cloud3.width=width
    cloud3.length=length
    cloud3.fill=color

def makeRain():
    # Creates new raindrops in storm
    raindrop = Group(Circle(200,60,10,fill='blue'),
                    RegularPolygon(200,50,10,3,fill='blue'))
    raindrop.centerX = randrange(1,400)
    rain.add(raindrop)

def drawLightning(startX):
    # Initiates a new lightning bolt
    if startX <= 300:    
        branchNumber = randrange(0,5) + 1
        for i in range(branchNumber):
            x1 = startX
            y1 = 50
            branchLength = randrange(5,10) + 1
            for i in range(branchLength):
                x2 = x1 + randrange(-15,15)
                y2 = y1 + randrange(10,20)
                branch = Line(x1,y1,x2,y2,fill=rgb(245,225,205),lineWidth=5)
                x1 = x2
                y1 = y2
                lightning.add(branch)

# onMousePress
def onMousePress(mouseX,mouseY):
    if app.stormActivate == True:
        app.background = gradient('lightGray','darkGray')
        grass.fill = 'lightGreen'
        sidewalk.fill = 'gold'
        app.currentStrike = True
        drawLightning(mouseX)

# onMouseRelease
def onMouseRelease(mouseX,mouseY):
    if app.stormActivate == True:
        app.background = 'darkBlue'
        grass.fill = 'green'
        sidewalk.fill = 'brown'
        app.currentStrike = False
        lightning.clear()

# onStep
def onStep():
    if app.stormDuration >= 100:
        app.stormActivate = True
        Clouds(100,300,'gray')
        if app.currentStrike == False:
            app.background = 'darkBlue'
            grass.fill = 'green'
            sidewalk.fill = 'brown'
        sun.visible = False
    if app.stormDuration >= 500:
        app.stormDuration = 0
        app.stormActivate = False
        app.currentStrike = False
        Clouds(50,150,'white')
        app.background = 'lightBlue'
        grass.fill = 'lightGreen'
        sidewalk.fill = 'gold'
        sun.visible = True
        lightning.clear()
    if app.stormActivate == True:
        if app.lightningRate == 0:
            app.background = gradient('lightGray','darkGray')
            grass.fill = 'lightGreen'
            sidewalk.fill = 'gold'
        app.lightningRate = randrange(0,50)
        makeRain()
    if lightning.hitsShape(car):
        car.opacity = 50
    else:
        car.opacity = 100
    for raindrop in rain:
        if raindrop.hitsShape(car) or raindrop.hitsShape(trafficLight) or raindrop.centerY >= 400:
            rain.remove(raindrop)
        else:
            raindrop.centerY += 10
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
    app.stormDuration += 1


cmu_graphics.run()
