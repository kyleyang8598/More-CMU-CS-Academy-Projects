'''
Descriptions: Big Wave Beach With Tides And Clouds
Instructions: Press 'l' to get a low tide, 'm' to get a medium tide, and 'h' to get a high tide.
You can also left click on your mouse or touchpad so you can turn a sunny day into a cloudy day.
'''

from cmu_graphics import *

# Globals
app.background = gradient('lightSteelBlue','skyBlue',start='top')
app.tidelength = 200
app.wavelength = 200

# Sand
sand = Rect(0,100,400,300,fill=gradient('paleGoldenRod','burlyWood',start='bottom'))

# Waves
wave1 = Rect(0,100,400,200,fill=gradient('darkBlue','darkBlue','darkBlue','darkBlue','white',start='top'))
wave2 = Rect(0,100,400,200,fill=gradient('darkBlue','darkBlue','darkBlue','darkBlue','white',start='top'))

wave1.angle = 180
wave2.angle = 0

# Sun
sun = Oval(375,25,100,100,fill=gradient('yellow','orange'),border='lightyellow',borderWidth=1)

# Clouds
cloud1 = Oval(50,25,150,50,fill='white')
cloud2 = Oval(150,25,150,50,fill='white')
cloud3 = Oval(250,25,150,50,fill='white')

def Clouds(length,width,color):
    cloud1.width=width
    cloud1.length=length
    cloud1.fill=color
    cloud2.width=width
    cloud2.length=length
    cloud2.fill=color
    cloud3.width=width
    cloud3.length=length
    cloud3.fill=color

# Blankets
blankets = Group()

def createBlankets():
    colors = ['red','orange','yellow','green','blue','violet']
    for i in range(6):
        blanket = Rect(90+i*40,350,20,40,fill=colors[i],border='white')
        blankets.add(blanket)

createBlankets()

blankets.visible = False

# Floaties
floaties = Group()

def createFloaties():
    colors = ['red','orange','yellow','green','blue','violet']
    for i in range(6):
        floatie = Oval(90+i*40,150,20,40,fill=colors[i],border='white')
        floaties.add(floatie)

createFloaties()

floaties.visible = False

# onMousePress
def onMousePress(mouseX,mouseY):
    sun.visible=False
    Clouds(100,300,'gray')

# onMouseRelease
def onMouseRelease(mouseX,mouseY):
    sun.visible=True
    Clouds(50,150,'white')
    
# onKeyPress
def onKeyPress(key):
    if key == 'l':
        app.tidelength = 150
    if key == 'm':
        app.tidelength = 200
    if key == 'h':
        app.tidelength = 250

# onStep
def onStep():
    wave1.height = app.wavelength + 50 * dsin(wave1.angle)
    wave1.angle += 3
    wave2.height = app.wavelength + 50 * dsin(wave2.angle)
    wave2.angle += 3
    if app.wavelength < app.tidelength:
        app.wavelength += 1
    if app.wavelength > app.tidelength:
        app.wavelength -= 1
    if dsin(wave1.angle) == -1:
        wave1.toFront()
    if dsin(wave2.angle) == -1:
        wave2.toFront()
    if app.wavelength == 150:
        blankets.visible = True
        floaties.visible = False
    if app.wavelength == 200:
        blankets.visible = False
        floaties.visible = False
    if app.wavelength == 250:
        blankets.visible = False
        floaties.visible = True
    blankets.toFront()
    floaties.toFront()


cmu_graphics.run()
