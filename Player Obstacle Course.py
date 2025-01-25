from cmu_graphics import *

# Background
app.background = 'darkGray'

# Difficulty
app.difficulty = 0

# Statistics
app.timeLength = 0
app.waveLength = 0

# Player
player = Group(Circle(200,200,25),
            Circle(200,200,20,fill='white'),
            Line(200,225,200,275,lineWidth=5),
            Line(175,250,200,225,lineWidth=5),
            Line(225,250,200,225,lineWidth=5),
            Line(200,275,175,300,lineWidth=5),
            Line(200,275,225,300,lineWidth=5),
            Circle(190,200,5),
            Circle(210,200,5))

player.visible = False
player.height /= 2
player.width /= 2

# Fireballs
fireballs = Group()

def summonFireball():
    colors = ['red','orange','yellow','green','blue']
    fireball = Star(randrange(60,340),-20,15,50)
    fireball.angle = angleTo(fireball.centerX,fireball.centerY,player.centerX,player.centerY)
    if app.difficulty == 1:
        fireball.speed = randrange(1,2)
    elif app.difficulty == 2:
        fireball.speed = randrange(1,3)
    elif 2 < app.difficulty < 6:
        fireball.speed = randrange(1,4)
    elif 5 < app.difficulty < 10:
        fireball.speed = randrange(1,5)
    else:
        fireball.speed = randrange(1,6)
    fireball.fill = colors[fireball.speed-1]
    fireballs.add(fireball)

# Cars
cars = Group()

def summonCar():
    car = Group(Polygon(25,125,75,75,125,75,175,125,fill='blue'),
            Rect(25,125,200,50,fill='orange'),
            Rect(75,80,50,40),
            Circle(75,175,25,fill='lightGray',border='gray',borderWidth=10),
            Circle(175,175,25,fill='lightGray',border='gray',borderWidth=10))
    if app.difficulty < 8:
        car.height /= 3
        car.width /= 3
    else:
        car.height /= 2
        car.width /= 2
    car.centerX = -50
    car.centerY = randrange(60,340)
    cars.add(car)

# Rockets
rockets = Group()

def summonRocket():
    rocket = Group(RegularPolygon(200,200,30,3,fill='violet',border='black'),
                Rect(180,215,40,150,fill='gray',border='black'),
                Polygon(180,300,180,250,150,300,fill='violet',border='black'),
                Polygon(220,300,220,250,250,300,fill='violet',border='black'),
                Polygon(180,365,220,365,220,405,200,385,180,405,fill=gradient('yellow','red')))
    if app.difficulty < 9:
        rocket.height /= 3
        rocket.width /= 3
    else:
        rocket.height /= 2
        rocket.width /= 2
    rocket.centerY = 460
    rocket.centerX = randrange(60,340)
    rockets.add(rocket)

# Cannons
cannons = Group()

def summonCannon():
    cannon = Circle(10,220,10,fill='brown')
    cannon.body = Group(Oval(20,200,50,30),
                Oval(40,200,10,30))
    cannon.ball = Circle(50,0,15,fill=gradient('white','black','black'),visible=False)
    cannon.fire = Polygon(40,170,60,170,55,180,60,190,40,190,fill=gradient('yellow','red'),visible=False)
    cannon.centerX = -40
    cannon.body.centerX = -30
    cannon.centerY = randrange(60,340) + 10
    cannon.body.centerY = cannon.centerY - 20
    cannon.energy = 0
    cannons.add(cannon)

# Snowflakes
snowflakes = Group()

def summonSnowflake():
    snowflake = Star(randrange(60,340),randrange(60,340),25,10,fill='white')
    snowflakes.add(snowflake)

# Player Data
healthLabel = Label('Health:',200,390,visible=False,bold=True)
app.health = 100
pointsLabel = Label('Points:',200,10,visible=False,bold=True)
app.points = 0
roundsLabel = Label('Rounds:',200,200,fill='darkRed',size=30,visible=False,bold=True)
app.rounds = 0
pointsScored = Label('Points Scored:',200,140,visible=False,bold=True)
roundsLasted = Label('Rounds Lasted:',200,170,visible=False,bold=True)
highestScoreLabel = Label('Highest Score:',200,200,visible=False,bold=True)
app.highestScore = 0
highestRoundLabel = Label('Highest Round:',200,230,visible=False,bold=True)
app.highestRound = 0

# Buttons
title = Label('Player Obstacle Course',200,100,size=30,bold=True)
start = Group(Rect(150,275,100,50),
            Label('Start',200,300,fill='white',size=30,bold=True))
again = Group(Rect(100,275,200,50),
            Label('Play Again',200,300,fill='white',size=30,bold=True),visible=False)
app.startGame = False

# onKeyHold
def onKeyHold(keys):
    if ('up' in keys) and player.centerY > 60:
        player.centerY -= 10
    if ('down' in keys) and player.centerY < 340:
        player.centerY += 10
    if ('left' in keys) and player.centerX > 60:
        player.centerX -= 10
    if ('right' in keys) and player.centerX < 340:
        player.centerX += 10

# onStep
def onStep():
    if app.startGame == True:    
        if app.timeLength == 40 - app.difficulty and app.waveLength != app.difficulty:
            roundsLabel.visible = False
            random = randrange(1,app.difficulty+1)
            if random <= 3:
                summonFireball()
            if random == 4 or random == 8:
                summonCar()
            if random == 5 or random == 9:
                summonRocket()
            if random == 6 or random >= 10:
                summonFireball()
            if random == 7:
                summonCannon()
            if random == randrange(1,app.difficulty+1):
                summonSnowflake()
            app.timeLength = 0
            app.waveLength += 1
        if app.timeLength == 200 - app.difficulty:
            app.timeLength = 0
            app.waveLength = 0
            app.difficulty += 1
            app.rounds = app.difficulty
            roundsLabel.value = 'Round ' + str(app.rounds)
            roundsLabel.size = 100
            roundsLabel.visible = True
        if roundsLabel.size != 30:
            roundsLabel.size -= 10
        if app.health <= 0:
            title.value = 'Game Over'
            app.startGame = False
            pointsLabel.visible = False
            healthLabel.visible = False
            player.visible = False
            title.visible = True
            start.visible = True
            again.visible = True
            pointsScored.value = 'Points Scored: ' + str(app.points)
            roundsLasted.value = 'Rounds Lasted: ' + str(app.rounds)
            pointsScored.visible = True
            roundsLasted.visible = True
            if app.points > app.highestScore:
                app.highestScore = app.points
            if app.rounds > app.highestRound:
                app.highestRound = app.rounds
            highestScoreLabel.value = 'Highest Score: ' + str(app.highestScore)
            highestScoreLabel.visible = True
            highestRoundLabel.value = 'Highest Round: ' + str(app.highestRound)
            highestRoundLabel.visible = True
            fireballs.clear()
            cars.clear()
            rockets.clear()
            cannons.clear()
            snowflakes.clear()
        healthLabel.value = 'Health: ' + str(app.health)
        for fireball in fireballs:
            fireball.centerX, fireball.centerY = getPointInDir(fireball.centerX,fireball.centerY,fireball.angle,fireball.speed*2)
            if fireball.hitsShape(player):
                app.health -= 10
                fireballs.remove(fireball)
            if fireball.top >= 400:
                fireballs.remove(fireball)
        for car in cars:
            car.centerX += 5
            if car.hitsShape(player):
                if app.difficulty <= 7:
                    app.health -= 10
                else:
                    app.health -= 20
                cars.remove(car)
            if car.left >= 400:
                cars.remove(car)
        for rocket in rockets:
            rocket.centerY -= 5
            if rocket.hitsShape(player):
                if app.difficulty <= 8:
                    app.health -= 10
                else:
                    app.health -= 20
                rockets.remove(rocket)
            if rocket.bottom <= 0:
                rockets.remove(rocket)
        for cannon in cannons:
            if cannon.energy >= 50:
                cannon.centerX -= 1
                cannon.body.centerX -= 1
                cannon.ball.centerX += 10
                cannon.fire.visible = False
                if cannon.ball.hitsShape(player):
                    app.health -= 20
                    cannon.ball.left = 400
                if cannon.body.right <= 0:
                    cannon.visible = False
                    cannon.body.visible = False
                    cannon.ball.visible = False
            if cannon.energy == 50:
                cannon.ball.visible = True
                cannon.fire.visible = True
                cannon.ball.centerY = cannon.body.centerY
                cannon.fire.centerY = cannon.body.centerY
            if cannon.energy <= 50:
                cannon.centerX += 1
                cannon.body.centerX += 1
            cannon.energy += 1
            if app.health <= 0:
                cannon.visible = False
                cannon.body.visible = False
                cannon.ball.visible = False
                cannon.fire.visible = False
        for snowflake in snowflakes:
            if snowflake.hitsShape(player):
                app.points += 1
                snowflakes.remove(snowflake)
        pointsLabel.value = 'Points: ' + str(app.points)
        app.timeLength += 1

# onMousePress
def onMousePress(mouseX,mouseY):
    if start.hits(mouseX,mouseY) and start.visible == True or again.hits(mouseX,mouseY) and again.visible == True:
        app.difficulty = 0
        app.timeLength = 0
        app.waveLength = 0
        app.startGame = True
        app.points = 0
        pointsLabel.value = 'Points: ' + str(app.points)
        pointsLabel.visible = True
        app.health = 100
        healthLabel.value = 'Health: ' + str(app.health)
        healthLabel.visible = True
        player.centerX = 200
        player.centerY = 200
        player.visible = True
        title.visible = False
        start.visible = False
        again.visible = False
        pointsScored.visible = False
        roundsLasted.visible = False
        highestScoreLabel.visible = False
        highestRoundLabel.visible = False


cmu_graphics.run()
