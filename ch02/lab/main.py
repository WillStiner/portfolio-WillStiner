import turtle  # 1. import modules
import random
import math

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. Your PART A code goes here

#Race 1
michelangelo.forward(random.randint(1, 101))
leonardo.forward(random.randint(1, 101))
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

#Race 2
for _ in range (10):
    michelangelo.forward(random.randrange(1, 11))
    leonardo.forward(random.randrange(1, 11))
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# PART B - complete part B here

#Triangle
leonardo.speed(5)
leonardo.goto(0, 50)
leonardo.down()
for _ in range (3):
    leonardo.forward(100)
    leonardo.right(360/3)
leonardo.clear()
leonardo.up()

#Square
leonardo.down()
for _ in range (4):
    leonardo.forward(100)
    leonardo.right(360/4)
leonardo.clear()
leonardo.up()

#Hexagon
leonardo.down()
for _ in range (6):
    leonardo.forward(100)
    leonardo.right(360/6)
leonardo.clear()
leonardo.up()

#Icosagon
leonardo.down()
for _ in range (20):
    leonardo.forward(50)
    leonardo.right(360/20)
leonardo.clear()
leonardo.up()

#Hectagon
leonardo.down()
for _ in range (100):
    leonardo.forward(10)
    leonardo.right(360/100)
leonardo.clear()
leonardo.up()

#Circle
leonardo.down()
for _ in range (360):
    leonardo.forward(3)
    leonardo.right(360/360)
leonardo.clear()
leonardo.up()

window.exitonclick()
