# Function defined: Line 20
# Function called 1: Line 68
# Function called 2: Line 78
# onMousePress: Line 60
# onMouseRelease: Line 70
# Property Change 1: Line 21
# Property Change 2: Line 22
# Property Change 3: Line 23
# Property Change 4: Line 61 and 71
# Property Change 5: Line 62 and 72

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
snow1 = Line(0,350,400,350,fill=None,lineWidth=20)
snow2 = Polygon(15,250,100,140,185,250,fill=None)
snow3 = RegularPolygon(325,195,85,3,fill=None)

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

def onMousePress(mouseX,mouseY):
    sun.visible=False
    snow1.fill='white'
    snow2.fill='white'
    snow3.fill='white'
    snowflakes1.visible=True
    snowflakes2.visible=True
    snowflakes3.visible=True
    Clouds(100,300,'gray')

def onMouseRelease(mouseX,mouseY):
    sun.visible=True
    snow1.fill=None
    snow2.fill=None
    snow3.fill=None
    snowflakes1.visible=False
    snowflakes2.visible=False
    snowflakes3.visible=False
    Clouds(50,150,'white')

# Frozen In Time: Depths of the Unknown
