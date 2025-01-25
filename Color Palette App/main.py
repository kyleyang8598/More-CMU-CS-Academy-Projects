'''
Directions: Drag the sliders to change each color with their RGBs.
Instructions: Press "space" for a random color and "tab" to reset.
'''

from cmu_graphics import *

app.background = rgb(230, 230, 230)
app.selected = None

for i in range(3):
    y = 35 + i * 50
    Label(0, 20, y, size=18, bold=True)
    Label(255, 380, y, size=18, bold=True)
    Rect(45, y - 16, 300, 32, fill=rgb(225, 225, 240), border='black', borderWidth=1),
    Circle(45, y, 16, fill=rgb(225, 225, 240), border='black', borderWidth=1),
    Circle(345, y, 16, fill=rgb(225, 225, 240), border='black', borderWidth=1),
    Rect(45, y - 15, 300, 30, fill=rgb(225, 225, 240))

redSlider = Circle(200, 35, 15, fill=rgb(125, 0, 0))
greenSlider = Circle(200, 85, 15, fill=rgb(0, 125, 0))
blueSlider = Circle(200, 135, 15, fill=rgb(0, 0, 125))
selectableItems = Group(redSlider, greenSlider, blueSlider)

c = Circle(200, 240, 70, fill=rgb(131, 131, 131), border='black')
c.label = Label('RGB', 200, 200, size=15, bold=True)
c.label1 = Label('Red: '+str(c.fill.red), 200, 230, size=15, bold=True)
c.label2 = Label('Green: '+str(c.fill.green), 200, 250, size=15, bold=True)
c.label3 = Label('Blue: '+str(c.fill.blue), 200, 270, size=15, bold=True)
c1 = Circle(65, 215, 45, fill=rgb(125, 125, 125), border='black', borderWidth=1)
c1.label = Label('GBR', 65, 215, size=15, bold=True)
c2 = Circle(335, 215, 45, fill=rgb(125, 125, 125), border='black', borderWidth=1)
c2.label = Label('BRG', 335, 215, size=15, bold=True)
c3 = Circle(65, 315, 45, fill=rgb(125, 125, 125), border='black', borderWidth=1)
c3.label = Label('GRB', 65, 315, size=15, bold=True)
c4 = Circle(335, 315, 45, fill=rgb(125, 125, 125), border='black', borderWidth=1)
c4.label = Label('BGR', 335, 315, size=15, bold=True)
c5 = Circle(200, 355, 45, fill=rgb(125, 125, 125), border='black', borderWidth=1)
c5.label = Label('RBG', 200, 355, size=15, bold=True)

def mapValue(value, valueMin, valueMax, targetMin, targetMax):
    ratio = (value - valueMin) / (valueMax - valueMin)
    result = ratio * (targetMax-targetMin) + targetMin
    return result

def getTriadicColors(color):
    color1 = rgb(color.green, color.blue, color.red)
    color2 = rgb(color.blue, color.red, color.green)
    color3 = rgb(color.green, color.red, color.blue)
    color4 = rgb(color.blue, color.green, color.red)
    color5 = rgb(color.red, color.blue, color.green)
    return color1, color2, color3, color4, color5

def updateFills():
    red = int(mapValue(redSlider.centerX, 45, 345, 0, 255))
    green = int(mapValue(greenSlider.centerX, 45, 345, 0, 255))
    blue = int(mapValue(blueSlider.centerX, 45, 345, 0, 255))
    redSlider.fill = rgb(red, 0, 0)
    greenSlider.fill = rgb(0, green, 0)
    blueSlider.fill = rgb(0, 0, blue)
    c.fill = rgb(redSlider.fill.red, greenSlider.fill.green, blueSlider.fill.blue)
    color1, color2 , color3, color4, color5 = getTriadicColors(c.fill)
    c1.fill = color1
    c2.fill = color2
    c3.fill = color3
    c4.fill = color4
    c5.fill = color5
    c.label1.value = 'Red: '+str(c.fill.red)
    c.label2.value = 'Green: '+str(c.fill.green)
    c.label3.value = 'Blue: '+str(c.fill.blue)

def onMousePress(mouseX, mouseY):
    app.selected = selectableItems.hitTest(mouseX, mouseY)
    if redSlider.contains(mouseX, mouseY):
        redSlider.opacity = 50
    if greenSlider.contains(mouseX, mouseY):
        greenSlider.opacity = 50
    if blueSlider.contains(mouseX, mouseY):
        blueSlider.opacity = 50

def onMouseRelease(mouseX, mouseY):
    if redSlider.contains(mouseX, mouseY):
        redSlider.opacity = 75
    if greenSlider.contains(mouseX, mouseY):
        greenSlider.opacity = 75
    if blueSlider.contains(mouseX, mouseY):
        blueSlider.opacity = 75

def onMouseMove(mouseX, mouseY):
    if redSlider.contains(mouseX, mouseY):
        redSlider.opacity = 75
    else:
        redSlider.opacity = 100
    if greenSlider.contains(mouseX, mouseY):
        greenSlider.opacity = 75
    else:
        greenSlider.opacity = 100
    if blueSlider.contains(mouseX, mouseY):
        blueSlider.opacity = 75
    else:
        blueSlider.opacity = 100

def onMouseDrag(mouseX, mouseY):
    if (app.selected != None):
        app.selected.centerX = mouseX
        if (app.selected.left < 30):
            app.selected.left = 30
        if (app.selected.right > 360):
            app.selected.right = 360
        updateFills()

def onKeyPress(key):
    if key == 'space':
        redSlider.centerX = randrange(45,346)
        greenSlider.centerX = randrange(45,346)
        blueSlider.centerX = randrange(45,346)
        updateFills()
    if key == 'tab':
        redSlider.centerX = 200
        greenSlider.centerX = 200
        blueSlider.centerX = 200
        updateFills()


cmu_graphics.run()
