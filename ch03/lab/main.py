import turtle
import random
import math 

turtle.setworldcoordinates(-1, -1, 1, 1)

window = turtle.Screen()
window.bgcolor("purple")

#draw the dartboard
pen = turtle.Turtle()
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
        pen.color("black")
        pen.dot(10)
    else:
        pen.color("red")
        pen.dot(10)

window.exitonclick()