import turtle
import random

turt = turtle.Turtle()
turt.speed(0)

window = turtle.Screen()
height = window.window_height() / 2
width = window.window_width() / 2

while abs(turt.xcor()) < width and abs(turt.ycor()) < width:
    coin = random.randint(0,1)
    if coin:
        turt.right(90)
        turt.forward(50)
    else:
        turt.left(90) 
        turt.forward(50)  