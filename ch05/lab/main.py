def threenp1(n):
    count = 0
    while n > 1.0:
        count = count + 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    starting_value = 2
    for _ in range (starting_value, upper_limit):
        count = threenp1(starting_value)
        threenp1(upper_limit)
        objs_in_sequence.update({starting_value : count})
        starting_value = starting_value + 1
        if starting_value == upper_limit:
            print(objs_in_sequence)
            return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    import turtle
    window = turtle.Screen()
    pos_x = 10
    pos_y = 10
    window.setworldcoordinates(0, 0, pos_x, pos_y)
            
    graph_pen = turtle.Turtle()
    graph_pen.speed(0)
    max_pen = turtle.Turtle()
    max_pen.speed(0)
    max_pen.penup()
    max_so_far = 0 
    starting_value = 2
    
    max_pen.goto(pos_x, pos_y)
    max_pen.write(max_so_far, font = ("Arial", 40, "normal"))
        
    for _ in threenplus1_iters_dict:
        graph_pen.goto(starting_value, threenplus1_iters_dict[starting_value])
        starting_value = starting_value + 1
        if max_so_far < graph_pen.ycor():
            max_so_far = graph_pen.ycor()
            max_pen.clear()
            max_pen.goto(pos_x - 10, max_so_far - 10)
            max_pen.write(max_so_far, font = ("Arial", 40, "normal"))
                    
        pos_x = pos_x + 1
        pos_y = max_so_far + 10

        window.setworldcoordinates(0, 0, pos_x, pos_y)
        
    window.exitonclick()      

def main():
    value = int(input("what would you like your largest number in the range to be?"))
    threenplus1_iters_dict = threenp1range(value)
    graph_coordinates(threenplus1_iters_dict)
    
main()