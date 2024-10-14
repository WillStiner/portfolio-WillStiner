import turtle

window = turtle.Screen()
pen = turtle.Turtle()
num_sides = int(input("how many sides?"))
side_length = int(input("how long the sides?"))
    
def draw_eq_shape(pen, num_sides, side_length):
    for _ in range (num_sides):
        pen.forward(side_length)
        pen.right(360/num_sides)
        
draw_eq_shape(pen, num_sides, side_length)

window.exitonclick()