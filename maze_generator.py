import turtle as t
import random


def jump_to(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def draw_background():
    t.setup(maze_size_x, maze_size_y)
    t.speed(50)
    jump_to(-(maze_size_x/ 2), -(maze_size_y / 2))
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.forward(maze_size_x)
        t.left(90)
        t.forward(maze_size_y)
        t.left(90)
    t.end_fill()


def draw_cell(coord_cell, color):
    x, y = coord_cell
    jump_to((-maze_size_x / 2) + (x + 1) * 20, (-maze_size_y / 2) + (y + 1) * 20)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()


def draw_end_bridge(end_neighbours):
    max_depth = 0
    deapest_cell = (0, 0)
    for x, y, depth in end_neighbours:
        if (depth > max_depth):
            max_depth = depth
            deapest_cell = (x, y)
    draw_cell(deapest_cell, "white")


def add_tuples(t1, t2):
    return((t1[0] + t2[0], t1[1] + t2[1]))


def cell_checker(cell, depth):
    global end_neighbours

    valid_cell = True
    # Checks if the maze goes out of bounds.
    if ((not (0 <= cell[0] < maze_x)) or (not (0 <= cell[1] < maze_y))):
        valid_cell = False

    # Checks if the maze goes back on itself.
    elif (cell in visited_cells):
        valid_cell = False

    # Checks if the maze will connect back on itself.
    else:
        neighbours = 0
        possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in possible_directions:
            neighbours_cell = add_tuples(cell, direction)
            if (neighbours_cell in visited_cells):
                neighbours += 1
                if (neighbours_cell == ending_cell):
                    end_neighbours.append((cell[0], cell[1], depth))
        if (neighbours > 1):
            valid_cell = False

    return(valid_cell)


def new_cell(current_cell, depth, facing):
    depth += 1
    if (depth == 1):
        color = "red"
    else:
        color = "white"
    draw_cell(current_cell, color)
    visited_cells.append(current_cell)

    if ((depth + 1) % 2 == 0):
        possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(possible_directions)
        for direction in possible_directions:
            cell = add_tuples(current_cell, direction)
            if (cell_checker(cell, depth)):
                new_cell(cell, depth, direction)

    else:
        cell = add_tuples(current_cell, facing)
        if (cell_checker(cell, depth)):
            new_cell(cell, depth, facing)

    # Only prints if none of the four neighbours of the current cell are valid
    # print("The maze is stuck")


maze_x = int(input("Width of the maze = ")) + 1
maze_y = int(input("height of the maze = ")) + 1
starting_cell_x = int(input("X coord of starting cell = "))
starting_cell_y = int(input("y coord of starting cell = "))
ending_cell_x = int(input("X coord of ending cell = "))
ending_cell_y = int(input("Y coord of ending cell = "))
ending_cell = (ending_cell_x, ending_cell_y)
starting_cell = (starting_cell_x, starting_cell_y)
maze_size_x = (maze_x + 2) * 20
maze_size_y = (maze_y + 2) * 20

draw_background()
visited_cells = []
end_neighbours = []
depth = 0
draw_cell(ending_cell, "green")
visited_cells.append(ending_cell)

new_cell(starting_cell, depth, (0, 1))
draw_end_bridge(end_neighbours)


# Pour éviter que le programme plante
while(1):
    t.left(0.1)
    t.right(0.1)