import turtle as t
import random


# Go to a specific place on the screen.
def jump_to(x, y):
    t.up()
    t.goto(x, y)
    t.down()


# Setup needed before drawing the maze.
def draw_background():
    t.setup(maze_size_x, maze_size_y)  # Sets screen size
    t.speed(50)
    jump_to(-(maze_size_x/ 2), -(maze_size_y / 2))  # Go to bottom left corner
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):  # Draw a big black rectangle for the background
        t.forward(maze_size_x)
        t.left(90)
        t.forward(maze_size_y)
        t.left(90)
    t.end_fill()


# Draws the cell 
def draw_cell(coord_cell, color):
    x, y = coord_cell
    # Go to the cell (convert the coordonates if the cell to the place on the creen)
    jump_to((-maze_size_x / 2) + (x + 1) * 20, (-maze_size_y / 2) + (y + 1) * 20)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()


# Draws the cell next to the ending that is the furthest away from the start
def draw_end_bridge(end_neighbours):
    max_depth = 0
    deapest_cell = (0, 0)
    for x, y, depth in end_neighbours:
        if (depth > max_depth):
            max_depth = depth
            deapest_cell = (x, y)
    draw_cell(deapest_cell, "white")


# Just a function to clean up some bits of the code
def add_tuples(t1, t2):
    return((t1[0] + t2[0], t1[1] + t2[1]))


# Function that checks if a cell can be drawn here
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

                # Checks if the cell is next to the ending
                if (neighbours_cell == ending_cell):
                    end_neighbours.append((cell[0], cell[1], depth))
        if (neighbours > 1):
            valid_cell = False

    return(valid_cell)


# Most important part if the programm
# It's a recursive function that will create a random path
# Once it's stuck and cannot go further, it will continue
# with a new branch off of the last drawn cell with a valid space next to it.
def new_cell(current_cell, depth, facing):
    depth += 1
    # draws the starting point in red
    if (depth == 1):
        color = "red"
    else:
        color = "white"
    draw_cell(current_cell, color)
    visited_cells.append(current_cell)

    # The path will try to change directions once every two turns to look cleaner
    if ((depth + 1) % 2 == 0):
        possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(possible_directions)
        # We try every neighbour cell possible but in a random order
        for direction in possible_directions:
            cell = add_tuples(current_cell, direction)
            if (cell_checker(cell, depth)):
                new_cell(cell, depth, direction)

    else:
        cell = add_tuples(current_cell, facing)
        if (cell_checker(cell, depth)):
            new_cell(cell, depth, facing)


# User input
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

# Starts generating the maze
new_cell(starting_cell, depth, (0, 1))
draw_end_bridge(end_neighbours)


# To prevent the programm from crashing.
while(1):
    t.left(0.1)
    t.right(0.1)
