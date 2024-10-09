
def star_pyramid():
    stars_in_row = "*"
    star = "*"
    rows = int(input("how many rows would you like in your pyramid?"))
    for _ in range(rows):
        print(stars_in_row)
        stars_in_row = stars_in_row + star

def rstar_pyramid():
    star = "*"
    rows = int(input("how many rows would you like in your pyramid?"))
    for _ in range(rows):
        print(star * rows)
        rows = rows - 1
        

star_pyramid()
rstar_pyramid()