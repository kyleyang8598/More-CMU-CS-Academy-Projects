from cmu_graphics import *

app.background = 'black'
app.stepsPerSecond = 5
app.luminescence = 0

fireflies = Group()

def makeFireflies():
    # Makes random numbers of fireflies in the fireflies group.
    for i in range(randrange(10,20)):    
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
        firefly.dx = randrange(-3,4)
        firefly.dy = randrange(-3,4)
        fireflies.add(firefly)

makeFireflies()
fireflies.opacity = 0

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
    if app.luminescence >= firefly.luminescence:
            firefly.luminescence += factor

def flyToOthers(firefly, othersCenter):
    factor = 0.005
    xDist = othersCenter[0] - firefly.centerX
    yDist = othersCenter[1] - firefly.centerY
    firefly.dx += xDist * factor
    firefly.dy += yDist * factor
    pass

def moveFirefly(firefly):
    # Moves the firefly.
    newX = firefly.centerX + firefly.dx
    newY = firefly.centerY + firefly.dy
    firefly.centerX = newX
    firefly.centerY = newY

    # Out of bounds.
    if (firefly.centerX > 400):
        firefly.centerX = 0
    if (firefly.centerX < 00):
        firefly.centerX = 400
    if (firefly.centerY > 400):
        firefly.centerY = 0
    if (firefly.centerY < 0):
        firefly.centerY = 400

def onStep():
    # Finds the other fireflies that are close, and finds the average of their centers.
    avg = getAverage()
    for firefly in fireflies:
        normalize(firefly,avg)
        if 800 <= firefly.luminescence <= 900:
            firefly.opacity = firefly.luminescence - 800
        if 900 <= firefly.luminescence <= 1000:
            firefly.opacity = 1000 - firefly.luminescence
        if firefly.luminescence >= 1000:
            firefly.luminescence = 0
            firefly.opacity = 0
        firefly.luminescence += 20
        avgCenter = [ 0, 0 ]
        totalfirefly = 0
        for firefly2 in fireflies:
            dist = distance(firefly.centerX, firefly.centerY, firefly2.centerX, firefly2.centerY)
            if (dist <= 30):
                avgCenter = [ avgCenter[0] + firefly2.centerX,
                              avgCenter[1] + firefly2.centerY ]
                totalfirefly += 1
        if (totalfirefly > 1):
            avgCenter = [ avgCenter[0] / totalfirefly, avgCenter[1] / totalfirefly ]
            flyToOthers(firefly, avgCenter)
        moveFirefly(firefly)


cmu_graphics.run()
