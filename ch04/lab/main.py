import turtle
import random
import math 

turtle.setworldcoordinates(-1, -1, 1, 1)

window = turtle.Screen()
window.bgcolor("purple")

pen = turtle.Turtle()

blue_score = 0
green_score = 0

#ask about the bet
bet = window.textinput("your bet", "which color do you think will win, blue or green?")
while bet != "blue" and bet != "green":
    bet = window.textinput("try again", "sorry, that's not a player color. blue or green?")
    
#draw the dartboard
pen.speed(0)
pen.penup()
pen.goto(0, 1)
pen.pendown()
pen.color("orange")
pen.begin_fill()
for _ in range (360):
    pen.forward(0.0173) #circumference divided by 360
    pen.right(1)
pen.end_fill()
pen.color("black")
pen.goto(0,-1)
pen.penup()
pen.goto(1,0)
pen.pendown()
pen.goto(-1,0)

#throw the darts
for _ in range (10):
    dart_x = random.uniform(1, -1)
    dart_y = random.uniform(1, -1)
    pen.penup()
    pen.goto(dart_x, dart_y)
    dart_distance = math.hypot(dart_x, dart_y)
    radius = 1

    if dart_distance <= radius:
        pen.color("blue")
        pen.dot(10)
        blue_score = blue_score + 1
    else:
        pen.color("red")
        pen.dot(10)
        
    
    dart_x = random.uniform(1, -1)
    dart_y = random.uniform(1, -1)
    pen.penup()
    pen.goto(dart_x, dart_y)
    dart_distance = math.hypot(dart_x, dart_y)
    radius = 1

    if dart_distance <= radius:
        pen.color("green")
        pen.dot(10)
        green_score = green_score + 1
    else:
        pen.color("red")
        pen.dot(10)

#print the results
pen.color("blue")
pen.goto(-.5, .5)
pen.write("blue score:", font = ("Arial", 20, "normal"))
pen.goto(-.5, .4)
pen.write(blue_score, font = ("Arial", 20, "normal"))

pen.color("green")
pen.goto(-.5, -.5)
pen.write("green score:", font = ("Arial", 20, "normal"))
pen.goto(-.5, -.6)
pen.write(green_score, font = ("Arial", 20, "normal"))

pen.goto(-.3, .1)
if blue_score > green_score:
    pen.color("blue")
    pen.write("blue wins!", font = ("Arial", 40, "normal"))
    if bet == "blue":
        pen.goto(-.3, -.1)
        pen.write("you won the bet!", font = ("Arial", 40, "normal"))
    else:
        pen.goto(-.3, -.1)
        pen.write("you lost the bet :(", font = ("Arial", 40, "normal"))
elif green_score > blue_score:
    pen.color("green")
    pen.write("green wins!", font = ("Arial", 40, "normal"))
    if bet == "blue":
        pen.goto(-.3, -.1)
        pen.write("you lost the bet :(", font = ("Arial", 40, "normal"))
    else:
        pen.goto(-.3, -.1)
        pen.write("you won the bet!", font = ("Arial", 40, "normal"))
else:
    pen.color("black")
    pen.write("tie!", font = ("Arial", 40, "normal"))
    pen.goto(-.6, -.1)
    pen.write("no one wins the bet :/", font = ("Arial", 40, "normal"))


window.exitonclick()