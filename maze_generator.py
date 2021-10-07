import turtle as t
import random


def draw_background():
    t.setup(500, 500)
    t.speed(50)
    jump(-250, -250)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.forward(500)
        t.left(90)
    t.end_fill()
    t.pencolor("white")
  

def jump(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def skip(d):
    t.up()
    t.forward(d)
    t.down()


def draw_cell(coord_cell):
    x, y = coord_cell
    jump(-250 + (x * 20), -250 + (y * 20))
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()


def add_tuples(t1, t2):
    return((t1[0] + t2[0], t1[1] + t2[1]))


def new_cell(current_cell, depth):
    depth += 1
    facing = (0, 1)
    draw_cell(current_cell)
    
    if (depth %2 == 0):
        possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        facing = possible_directions[random.randint(0, 3)]

    next_cell = add_tuples(current_cell, facing)
    new_cell(next_cell, depth)

draw_background()
visited_cells = []
current_cell = (0, 0)
depth = 0
new_cell(current_cell, depth)


# Pour éviter que le programme plante
while(1):
    t.left(0.1)
    t.right(0.1)

