from cmu_graphics import *

# Background
app.background = 'lightGreen'

# Water
Rect(0,0,400,100,fill='aqua')

# Road
Rect(0,150,400,100)
Line(0,200,400,200,fill='yellow',dashes=True)

# Traffic Lights
Rect(175,275,50,100,fill='gray')
redLight = Circle(200,300,20,fill='darkRed')
greenLight = Circle(200,350,20,fill='darkGreen')

# Car
carTop = Polygon(125,125,175,75,225,75,275,125,fill='blue')
carBottom = Rect(125,125,200,50,fill='orange',)
carWindow = Rect(175,80,50,40)
wheel1 = Circle(175,175,25,fill='lightGray',border='gray',borderWidth=10)
wheel2 = Circle(275,175,25,fill='lightGray',border='gray',borderWidth=10)

# Movement
def moveCar(location):
    carTop.centerX = location
    carBottom.centerX = location + 25
    carWindow.centerX = location
    wheel1.centerX = location - 25
    wheel2.centerX = location + 75

# Drag Function
def onMouseDrag(mouseX,mouseY):
    if carWindow.centerX == 500:
        carWindow.centerX = -100
        moveCar(carWindow.centerX)
    else:
        carWindow.centerX += 1
        moveCar(carWindow.centerX)

# Press Function
def onMousePress(mouseX,mouseY):
    greenLight.fill = 'lime'
    redLight.fill = 'darkRed'

# Release Function
def onMouseRelease(mouseX,mouseY):
    greenLight.fill = 'darkGreen'
    redLight.fill = 'red'

# Travel Time!: Traffic Car!


cmu_graphics.run()
