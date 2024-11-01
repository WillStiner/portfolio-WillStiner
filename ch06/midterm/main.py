import turtle

def determine_condiment(condiment):
    '''
    determines if the user wants to look at ketchup or mustard, and returns the necessary color
    args: condiment (string), the user's input
    return: condiment_color (string), the color needed for the drawing
    '''
    if condiment == "ketchup":
        condiment_color = "red"
        return condiment_color
    else:
        condiment_color = "yellow"
        return condiment_color    

    
def draw_bottle(condiment_color):
    '''
    uses the turtle to draw the condiment bottle
    args: condiment_color (string), the color needed for the drawing
    return: N/A
    '''
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    x_cor = 0
    y_cor = 0
    bottle_x_cor = -2
    bottle_y_cor = 4
    pen.pencolor(condiment_color)
    pen.color(condiment_color)
    pen_size = 5
    pen.pensize(pen_size)
    pen.goto(bottle_x_cor, bottle_y_cor)
    pen.pendown()
    pen.begin_fill()
    turn_angle = 90
    bottle_length = 10
    bottle_width = 3
    for _ in range (2):
        pen.forward(bottle_width)
        pen.right(turn_angle)
        pen.forward(bottle_length)
        pen.right(turn_angle)
    pen.forward(bottle_width / 3)
    pen.left(turn_angle)
    pen.forward(bottle_width / 3)
    pen.right(turn_angle)
    pen.forward(bottle_width / 6)
    pen.left(turn_angle)
    pen.forward(bottle_width / 1.5)
    pen.right(turn_angle * 2)
    pen.forward(bottle_width / 1.5)
    pen.left(turn_angle)
    pen.forward(bottle_width / 6)
    pen.right(turn_angle)
    pen.forward(bottle_width / 3)
    pen.end_fill()
    pen.goto(x_cor, y_cor)
    pen.pencolor("black")
    circle_sides = 360
    circle_sides_length = .008
    circle_sides_angle = 1
    for _ in range (circle_sides):
        pen.forward(circle_sides_length)
        pen.right(circle_sides_angle)
    pen.penup()
    letter_xcor = -.65
    letter_ycor = -.35
    pen.goto(letter_xcor, letter_ycor)
    font_size = 15
    if condiment_color == "red":
        pen.write("K", font = ("Arial", font_size, "normal"))
    else:
        pen.write("M", font = ("Arial", font_size, "normal"))
    go_away_coor = 20    
    pen.goto(go_away_coor, go_away_coor)
        
def main():
    window = turtle.Screen()
    window.setworldcoordinates(-10, -10, 10, 10)
    
    condiment = window.textinput("hello", "what'll it be fellas, mustard or ketchup?")
    while condiment != "ketchup" and condiment != "mustard":
        condiment = window.textinput("you got this", "you gotta pick mustard or ketchup man. give it another go. please")

    condiment_color = determine_condiment(condiment)
    draw_bottle(condiment_color)
    
    window.exitonclick()
    
main()