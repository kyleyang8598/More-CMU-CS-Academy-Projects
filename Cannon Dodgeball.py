# Player
playerHead = Circle(200,200,10,fill=None,border='black')
playerBody = Line(200,210,200,230)
playerArms = Line(190,220,210,220)
playerLeg1 = Line(200,230,190,240)
playerLeg2 = Line(200,230,210,240)

def Player(locationX,locationY):
    playerHead.centerX = locationX
    playerHead.centerY = locationY
    playerBody.centerX = locationX
    playerBody.centerY = locationY + 20
    playerArms.centerX = locationX
    playerArms.centerY = locationY + 20
    playerLeg1.centerX = locationX - 5
    playerLeg1.centerY = locationY + 35
    playerLeg2.centerX = locationX + 5
    playerLeg2.centerY = locationY + 35

# Cannon
leftCannonWheel = Circle(10,220,10,fill='brown')
leftCannonHead = Oval(40,200,10,30)
leftCannonBody = Oval(20,200,50,30,)
rightCannonWheel = Circle(390,220,10,fill='brown')
rightCannonHead = Oval(360,200,10,30)
rightCannonBody = Oval(380,200,50,30)

def Cannon(location):
    leftCannonWheel.centerY = location
    leftCannonHead.centerY = location - 20
    leftCannonBody.centerY = location - 20
    rightCannonWheel.centerY = location
    rightCannonHead.centerY = location - 20
    rightCannonBody.centerY = location - 20

# Cannon Ball
cannonBall = Circle(0,0,15,fill=gradient('white','black','black'),visible=False)
cannonBall.direction = 1
cannonBall.energy = 0
cannonBall.power = 10
cannonBall.speed = 20

# Cannon Fire
cannonFire1 = Polygon(40,170,60,170,55,180,60,190,40,190,fill=gradient('yellow','red'),visible=False)
cannonFire2 = Polygon(360,170,340,170,345,180,340,190,360,190,fill=gradient('yellow','red'),visible=False)

def cannonFire():
    cannonBall.visible = True
    cannonBall.centerY = playerHead.centerY
    cannonBall.energy = 0
    cannonBall.power += 1
    cannonBall.speed += 2
    if cannonBall.direction == 1:
        cannonFire1.visible = True
        cannonFire1.centerY = playerHead.centerY
        cannonBall.toFront()
        cannonBall.centerX = 50
        cannonBall.direction = 2
    elif cannonBall.direction == 2:
        cannonFire2.visible = True
        cannonFire2.centerY = playerHead.centerY
        cannonFire2.toBack()
        cannonBall.centerX = 350
        cannonBall.direction = 1

# Player Data
Label('Points:',180,10)
points = Label(0,220,10)
Label('Health:',180,390)
health = Label(200,220,390)

def healthDown():
    if cannonBall.containsShape(playerHead):
        health.value -= cannonBall.power * 2
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0
    elif cannonBall.hitsShape(playerHead):
        health.value -= cannonBall.power
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0
    elif cannonBall.hitsShape(playerBody):
        health.value -= cannonBall.power
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0
    elif cannonBall.hitsShape(playerArms):
        health.value -= cannonBall.power
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0
    elif cannonBall.hitsShape(playerLeg1):
        health.value -= cannonBall.power
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0
    elif cannonBall.hitsShape(playerLeg2):
        health.value -= cannonBall.power
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0

# OnKeyPress
def onKeyPress(key):
    if (key == 'up'):
        cannonBall.energy += 1
        if playerHead.centerY > 60:
            playerHead.centerY -= 10
            Player(playerHead.centerX,playerHead.centerY)
            Cannon(playerHead.centerY+20)
        if cannonBall.energy == 10:
            points.value += 1
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        healthDown()
    elif (key == 'down'):
        cannonBall.energy += 1
        if playerHead.centerY < 340:
            playerHead.centerY += 10
            Player(playerHead.centerX,playerHead.centerY)
            Cannon(playerHead.centerY+20)
        if cannonBall.energy == 10:
            points.value += 1
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        healthDown()
    elif (key == 'left'):
        cannonBall.energy += 1
        if playerHead.centerX > 60:
            playerHead.centerX -= 10
            Player(playerHead.centerX,playerHead.centerY)
        if cannonBall.energy == 10:
            points.value += 1
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        healthDown()
    elif (key == 'right'):
        cannonBall.energy += 1
        if playerHead.centerX < 340:
            playerHead.centerX += 10
            Player(playerHead.centerX,playerHead.centerY)
        if cannonBall.energy == 10:
            points.value += 1
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        healthDown()
    else:
        cannonBall.energy += 1
        if cannonBall.energy == 10:
            points.value += 1
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        healthDown()
    if health.value <= 0:
        health.value = 0
        Label('Game Over',200,200,size=50)
        app.stop()

# OnKeyRelease            
def onKeyRelease(key):
    cannonFire1.visible = False
    cannonFire2.visible = False

# Cannon Dodgeball
