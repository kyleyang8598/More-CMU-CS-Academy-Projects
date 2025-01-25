'''
Author: Kyle Yang
Creation Date: October 16
Last Modified: October 19
Project Description: Weather cycles and daylight cycles occur over an open landscape.
Instructions: Left click the mouse to initiate a lightning strike somewhere.
(You can only initiate a lightning strike when it's raining)
Credits: None
Updates: None
Rubric Item:
    Color:
        Colors change: Line 162, Line 169, Line 180, Line 192, Line 201, Line 204, Line 210, Line 213.
        Specific scheme coded: Line 63, Line 68, Line 152.
        Colors change based on coded scheme: Line 204, Line 213.
    Patterns:
        Patterns created: Line 78, Line 114.
        Loops used to create pattern: Line 80, Line 116.
        Includes oscillating effect: Line 224.
    Generative Art:
        Art is generated during app operation: Line 98, Line 164.
        Randomness is included: Line 101, Line 105, Line 107, Line 108.
        3 or more rules used to generate the art: Line 101, Line 105, Line 107, Line 108.
    Emergent Behavior:
        Elements begin with independent behavior: Line 131.
        Interaction between elements is easily observable: Line 136, Line 144.
        Complex or group behavior results from interaction: Line 148, Line 149, Line 150.
'''

from cmu_graphics import *

def main():
    makeLandscape()
    makeClouds()
    app.cycleStarted = True

# Globals
app.cycleStarted = False
app.luminescence = 0
app.dayLightCycle = 0
app.lightningRate = 0
app.stormActivate = False
app.currentStrike = False
app.stepsPerSecond = 10
app.background = rgb(0,250,250)

# Groups

# Landscape
landscape = Group()

# Clouds
clouds = Group()

# Rain
rain = Group()

# Lightning
lightning = Group()

# Fireflies
fireflies = Group()

# Functions

def makeLandscape():
    # Designs new landscape.
    for i in range(1, 6):
        startY = 100 + i * 50
        # Gets a color that is in the landscape's monochromatic scheme.
        color = getMonochromaticColor(rgb(0,250,0), 1 - i / 10)
        layer = Polygon(0, 410, 0, startY, fill=color)
        y = startY
        for i in range(50):
            x = 10 * i
            y += randrange(-5, 5)
            layer.addPoint(x, y)
        layer.addPoint(405, 410)
        landscape.add(layer)

def makeClouds():
    # Generates more clouds.
    for i in range(3):
        cloud = Oval(i*100+50,25,150,50,fill='white')
        clouds.add(cloud)

def modifyClouds(length,width,color):
    # Changes clouds' color and size.
    for cloud in clouds:
        cloud.width=width
        cloud.length=length
        cloud.fill=color

def makeRain():
    # Creates new raindrops in storm.
    raindrop = Group(Circle(200,60,10,fill='blue'),
                    RegularPolygon(200,50,10,3,fill='blue'))
    raindrop.centerX = randrange(1,400)
    rain.add(raindrop)

def drawLightning(startX):
    # Initiates a new lightning bolt.
    if startX <= 300:    
        branchNumber = randrange(5,10)
        for i in range(branchNumber):
            x1 = startX
            y1 = 50
            branchLength = randrange(10,20)
            for i in range(branchLength):
                x2 = x1 + randrange(-15,15)
                y2 = y1 + randrange(10,20)
                branch = Line(x1,y1,x2,y2,fill=rgb(245,225,205),lineWidth=5)
                x1 = x2
                y1 = y2
                lightning.add(branch)

def makeFireflies():
    # Makes random numbers of fireflies in the fireflies group.
    for i in range(10):    
        firefly = Group(Line(195,165,190,155,fill='green'),
                        Line(205,165,210,155,fill='green'),
                        Circle(190,150,5,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                        Circle(210,150,5,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                        Circle(180,185,15,fill=gradient('gray','white',start='right')),
                        Circle(220,185,15,fill=gradient('gray','white',start='left')),
                        Oval(180,185,20,10,fill='gray'),
                        Oval(220,185,20,10,fill='gray'),
                        Circle(200,200,15,fill=gradient('lightYellow','yellow',start='bottom'),border='yellow'),
                        Circle(200,175,15,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                        Circle(190,175,5,fill='white'),
                        Circle(210,175,5,fill='white'),
                        Circle(190,175,3,fill='black'),
                        Circle(210,175,3,fill='black'))
        firefly.luminescence = randrange(0,1000)
        firefly.centerX = randrange(1,400)
        firefly.centerY = randrange(1,400)
        fireflies.add(firefly)

def getAverage():
    # Returns the average luminescence of the fireflies. They are stored in the fireflies group.
    total = 0
    for firefly in fireflies:
        total += firefly.luminescence
    average = total / len(fireflies)
    return average

def normalize(firefly,avg):
    # The factor affects how quickly the fireflies synchronize.
    factor = 10
    # Gets how far the luminescence is from average, then adds the factor to luminescence value.
    app.luminescence += (avg - app.luminescence)
    if app.luminescence > firefly.luminescence:
            firefly.luminescence += factor

def getMonochromaticColor(color, ratio):
    # Gets a new color in the same monochromatic scheme as the provided color.
    newColor = rgb(int(color.red * ratio),
                   int(color.green * ratio),
                   int(color.blue * ratio))
    return newColor

# onMousePress
def onMousePress(mouseX,mouseY):
    if app.stormActivate == True:
        app.background = gradient('lightGray','darkGray')
        app.currentStrike = True
        drawLightning(mouseX)

# onMouseRelease
def onMouseRelease(mouseX,mouseY):
    if app.stormActivate == True:
        app.background = 'darkBlue'
        app.currentStrike = False
        lightning.clear()

# onStep
def onStep():
    if app.cycleStarted == True:
        if 50 < app.dayLightCycle <= 150:
            app.stormActivate = True
            modifyClouds(100,300,'gray')
            if app.currentStrike == False:
                app.background = 'darkBlue'
            fireflies.clear()
            landscape.opacity = 20
        if 150 < app.dayLightCycle <= 200:
            app.stormActivate = False
            app.currentStrike = False
            modifyClouds(50,150,'white')
            app.background = rgb(0,250,250)
            lightning.clear()
            landscape.opacity = 100
        if app.stormActivate == True:
            if app.lightningRate == 0:
                app.background = gradient('lightGray','darkGray')
            app.lightningRate = randrange(0,50)
            makeRain()
        for raindrop in rain:
            if raindrop.centerY > 400:
                rain.remove(raindrop)
            else:
                raindrop.centerY += 10
        if 200 < app.dayLightCycle <= 250:
            app.background = rgb(0,app.background.green-5,app.background.blue-5)
            clouds.visible = False
            for layer in landscape:
                layer.fill = rgb(0,layer.fill.green-2,0)
        if app.dayLightCycle == 250:
            app.luminescence = 0
            makeFireflies()
            fireflies.opacity = 0
        if 450 < app.dayLightCycle <= 500:
            app.background = rgb(0,app.background.green+5,app.background.blue+5)
            fireflies.clear()
            for layer in landscape:
                layer.fill = rgb(0,layer.fill.green+2,0)
        if app.dayLightCycle > 500:
            clouds.visible = True
            app.dayLightCycle = 0
        app.dayLightCycle += 1
        # Finds the other fireflies that are close, and finds the average of their centers.
        if len(fireflies) > 0:
            avg = getAverage()
            for firefly in fireflies:
                normalize(firefly,avg)
                if 720 < firefly.luminescence <= 900:
                    firefly.opacity = dsin(firefly.luminescence) * 100
                if firefly.luminescence > 900:
                    firefly.luminescence = 0
                    firefly.opacity = 0
                firefly.luminescence += 20

main()


cmu_graphics.run()
