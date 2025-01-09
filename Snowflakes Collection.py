# Background
app.background = 'skyBlue'

# Player
playerHead = Circle(200,200,10,fill='white',border='black',)
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

# Snowflakes
snowFlakes = Star(0,0,25,10,fill='white',visible=False)

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

# Cannon Fire
cannonFire1 = Polygon(40,170,60,170,55,180,60,190,40,190,fill=gradient('yellow','red'),visible=False)
cannonFire2 = Polygon(360,170,340,170,345,180,340,190,360,190,fill=gradient('yellow','red'),visible=False)

# Cannon Ball
cannonBall = Circle(0,0,15,fill=gradient('white','black','black'),visible=False)
cannonBall.direction = 1
cannonBall.energy = 0
cannonBall.power = 10
cannonBall.speed = 10

def cannonFire():
    cannonBall.visible = True
    cannonBall.centerY = playerHead.centerY
    cannonBall.energy = 0
    snowFlakes.visible = True
    snowFlakes.centerX = 400 - playerHead.centerX
    snowFlakes.centerY = 400 - playerHead.centerY
    if cannonBall.direction == 1:
        cannonFire1.visible = True
        cannonFire1.centerY = playerHead.centerY
        cannonBall.centerX = 50
        cannonBall.direction = 2
    elif cannonBall.direction == 2:
        cannonFire2.visible = True
        cannonFire2.centerY = playerHead.centerY
        cannonBall.centerX = 350
        cannonBall.direction = 1

# Player Data
Label('Points:',180,10)
points = Label(0,220,10)
Label('Health:',180,390)
health = Label(200,220,390)

def healthDown():
    if cannonBall.hitsShape(playerHead) or cannonBall.hitsShape(playerBody) or cannonBall.hitsShape(playerArms) or cannonBall.hitsShape(playerLeg1) or cannonBall.hitsShape(playerLeg2):
        if not cannonBall.hitsShape(playerHead):
            health.value -= cannonBall.power
        else:
            health.value -= cannonBall.power * 2
        cannonBall.visible = False
        cannonBall.centerX = 0
        cannonBall.centerY = 0

# OnKeyHold
def onKeyHold(keys):
    if ('up' in keys) or ('down' in keys) or ('left' in keys) or ('right' in keys):
        cannonBall.energy += 1
        if ('up' in keys) and playerHead.centerY > 60:
            playerHead.centerY -= 10
        if ('down' in keys) and playerHead.centerY < 340:
            playerHead.centerY += 10
        if ('left' in keys) and playerHead.centerX > 60:
            playerHead.centerX -= 10
        if ('right' in keys) and playerHead.centerX < 340:
            playerHead.centerX += 10
        Player(playerHead.centerX,playerHead.centerY)
        Cannon(playerHead.centerY+20)
        cannonFire1.visible = False
        cannonFire2.visible = False
        if cannonBall.energy == 50:
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        if snowFlakes.hitsShape(playerHead) or snowFlakes.hitsShape(playerBody) or snowFlakes.hitsShape(playerArms) or snowFlakes.hitsShape(playerLeg1) or snowFlakes.hitsShape(playerLeg2):
            points.value += 1
            cannonBall.power += 1
            cannonBall.speed += 1
            snowFlakes.visible = False
            snowFlakes.centerX = 0
            snowFlakes.centerY = 0
        healthDown()
    else:
        cannonBall.energy += 1
        if ('up' in keys) and playerHead.centerY > 60:
            playerHead.centerY -= 10
        if ('down' in keys) and playerHead.centerY < 340:
            playerHead.centerY += 10
        if ('left' in keys) and playerHead.centerX > 60:
            playerHead.centerX -= 10
        if ('right' in keys) and playerHead.centerX < 340:
            playerHead.centerX += 10
        Player(playerHead.centerX,playerHead.centerY)
        Cannon(playerHead.centerY+20)
        cannonFire1.visible = False
        cannonFire2.visible = False
        if cannonBall.energy == 50:
            cannonFire()
        if cannonBall.direction == 1:
            cannonBall.centerX -= cannonBall.speed
        if cannonBall.direction == 2:
            cannonBall.centerX += cannonBall.speed
        if snowFlakes.hitsShape(playerHead) or snowFlakes.hitsShape(playerBody) or snowFlakes.hitsShape(playerArms) or snowFlakes.hitsShape(playerLeg1) or snowFlakes.hitsShape(playerLeg2):
            points.value += 1
            cannonBall.power += 1
            cannonBall.speed += 1
            snowFlakes.visible = False
            snowFlakes.centerX = 0
            snowFlakes.centerY = 0
        healthDown()
    if health.value <= 0:
        health.value = 0
        Label('Game Over',200,200,size=50)
        app.stop()

# Snowflakes Collection
