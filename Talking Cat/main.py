# Kyle Yang
# Project Description: A robotic cat that responds to your questions and messages. The cat version of an Amazon Echo or Google Home.
# Instructions: Press space to talk to the cat and ask questions. Press tab to make a custom message for the cat.
# You can also ask questions like "How are you?", "What is your favorite food?", and "What is your favorite color?".
# String List: Lines 22-26, 95-98
# Function with Return & For Loop: Lines 28-30, 32-34, 80-82
# While Loop: Line 40

from cmu_graphics import *

cat = Group(Circle(200,200,100,fill='orange',border='black'),
            RegularPolygon(125,100,50,3,fill='darkOrange',border='black',rotateAngle=90),
            RegularPolygon(275,100,50,3,fill='darkOrange',border='black',rotateAngle=270),
            RegularPolygon(125,100,30,3,fill='orangeRed',border='black',rotateAngle=90),
            RegularPolygon(275,100,30,3,fill='orangeRed',border='black',rotateAngle=270),
            Circle(200,210,50),
            Oval(200,200,150,100,fill='orange'),
            Circle(150,150,25,fill='white',border='black'),
            Circle(250,150,25,fill='white',border='black'),
            Circle(150,150,10),
            Circle(250,150,10))

text = Label("",200,350)
greetings = ["Hi", "Hello", "What's up"]
exclamations = ["Cool!", "Nice!", "Ok!", "That's awesome!", "Wow!"]
incorrections = ["Nice Try!", "Nope!", "Incorrect!", "Wrong!", "Haha! I guess you'll never know!"]
customMessages = []
customResponses = []

def getRandomGreeting():
    greeting = choice(greetings)
    return greeting

def getRandomExclamation():
    exclamation = choice(exclamations)
    return exclamation

app.guesses = 0
app.catName = ""
app.message = ""

while len(app.catName) == 0:
    app.catName = app.getTextInput("What is your name?")
    if len(app.catName) != 0:
        app.message = getRandomGreeting() + ", Press 'space' to ask questions. Press 'tab' to add messages."
        text.value = ""

# onStep
def onStep():
    if len(text.value) < len(app.message):
        text.value += app.message[len(text.value)]
    else:
        if app.message == "I'm feeling great! How about you?":
            feeling = app.getTextInput("How are you?")
            app.message = feeling + "? " + getRandomExclamation()
            text.value = ""
        if app.message == "Guess! Or you'll never know the answer!" or app.message in incorrections:
            if app.guesses < 5:
                guess = app.getTextInput("What is the cat's favorite food?")
                if guess == 'Fish':
                    app.message = "Correct! You got it right! My favorite food is fish."
                else:
                    app.message = incorrections[app.guesses]
                    app.guesses += 1
            else:
                app.message = "Okay, fine! I'll tell you! My favorite food is fish."
                app.guesses = 0
            text.value = ""
        if app.message == "My favorite color is orange. What is your favorite color?":
            color = app.getTextInput("What it your favorite color?")
            if color == "Orange":
                app.message = getRandomExclamation() + " My favorite color is orange too!"
            else:
                app.message = color + "? " + getRandomExclamation()
            text.value = ""

# onKeyPress
def onKeyPress(key):
    if key == 'space':
        question = app.getTextInput("Say Something:")
        if question in customMessages:
            for i in range(len(customMessages)):
                if question == customMessages[i]:
                    app.message = customResponses[i]
        elif question in greetings:
            app.message = getRandomGreeting() + ", " + app.catName
        elif question == "How are you?":
            app.message = "I'm feeling great! How about you?"
        elif question == "What is your favorite food?":
            app.message = "Guess! Or you'll never know the answer!"
        elif question == "What is your favorite color?":
            app.message = "My favorite color is orange. What is your favorite color?"
        else:        
            app.message = getRandomExclamation()
        text.value = ""
    if key == 'tab':
        message = app.getTextInput("What should the message be?")
        response = app.getTextInput("What should the response be?")
        customMessages.append(message)
        customResponses.append(response)

# Talking Cat


cmu_graphics.run()
