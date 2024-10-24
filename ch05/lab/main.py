
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
            pass

def graph_coordinates(objs_in_sequence):
    import turtle
    window = turtle.Screen()
    window.setworldcoordinates(0, 0, 10, 10)
            
    graph_pen = turtle.Turtle()
    graph_pen.speed(0)
    graph_pen.goto(objs_in_sequence)
    max_pen = turtle.Turtle()
    max_pen.speed(0)
    
    max_so_far = 0 
    

def main():
    value = 72
    threenp1range(value)        
      
main()