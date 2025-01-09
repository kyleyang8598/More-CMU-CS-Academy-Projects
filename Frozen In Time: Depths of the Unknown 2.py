from cmu_graphics import *

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

# Snowflakes
snowflakes1 = Star(50,100,25,10,fill='white',visible=False)
snowflakes2 = Star(150,100,25,10,fill='white',visible=False)
snowflakes3 = Star(250,100,25,10,fill='white',visible=False)

# Snow
snow1 = Line(0,360,400,360,fill='white',lineWidth=20)
snow2 = Polygon(25,250,100,150,175,250,fill='white')
snow3 = RegularPolygon(325,200,75,3,fill='white')

# Ground
Rect(0,350,400,50,fill='saddleBrown')

# Pine Tree
Rect(300,250,50,100,fill=rgb(160,82,45))
RegularPolygon(325,200,75,3,fill='green')
RegularPolygon(325,250,75,3,fill='green')

# House
Rect(50,250,100,100,fill='brown')
Polygon(25,250,175,250,100,150,fill=rgb(160,82,45))

# Door
Rect(75,275,50,75,fill=rgb(160,82,45))
Circle(115,315,5,fill='saddleBrown')

# Background
app.background='skyBlue'

def onMouseMove(mouseX,mouseY):
    if snow1.height > 20:    
        snow1.height-=1
        snow2.height-=1
        snow3.height-=1
        snow2.width-=1
        snow3.width-=1
        snow1.centerY+=1/2
        snow2.centerY+=1/2
        snow3.centerY+=1/3

def onMouseDrag(mouseX,mouseY):
    if snow1.height < 100:
        snow1.height+=1
        snow2.height+=1
        snow3.height+=1
        snow2.width+=1
        snow3.width+=1
        snow1.centerY-=1/2
        snow2.centerY-=1/2
        snow3.centerY-=1/3
        if snowflakes1.centerY < 300:
            snowflakes1.centerY+=10
            snowflakes2.centerY+=10
            snowflakes3.centerY+=10
        else:
            snowflakes1.centerY=100
            snowflakes2.centerY=100
            snowflakes3.centerY=100
    else:
        snowflakes1.visible=False
        snowflakes2.visible=False
        snowflakes3.visible=False

def onMousePress(mouseX,mouseY):
    sun.visible=False
    snowflakes1.visible=True
    snowflakes2.visible=True
    snowflakes3.visible=True
    snowflakes1.centerY=100
    snowflakes2.centerY=100
    snowflakes3.centerY=100
    Clouds(100,300,'gray')

def onMouseRelease(mouseX,mouseY):
    sun.visible=True
    snowflakes1.visible=False
    snowflakes2.visible=False
    snowflakes3.visible=False
    Clouds(50,150,'white')

# Frozen In Time: Depths of the Unknown 2


cmu_graphics.run()
