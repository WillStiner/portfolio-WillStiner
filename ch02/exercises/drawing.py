import turtle

num_of_sides = int(input("how many sides will your shape have?"))
len_of_sides = int(input("how long will the lengths of the sides be?"))
pen_angle = 360 / num_of_sides

pen = turtle.Turtle()
screen = turtle.Screen()

pen.color("orange")
pen.shape("turtle")

for _ in range (num_of_sides):
    pen.forward(len_of_sides)
    pen.right(pen_angle)

screen.exitonclick()