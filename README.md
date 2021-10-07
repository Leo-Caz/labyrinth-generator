# maze-generator
A small project for my programming class.

I'm using turtle to render everything on screen because that is one of the requierments for the assignement.

For now I just have the code needed to get something to reder on the screen and create a completely random path (with no way to prevent it to go off screen or go back on itself). My general idea for this project is to use a recursive function to create a cell, create another cell in front of the one previously placed and periodically turning around in a random direction (or just stay in the same direction). The programm will make sure not to go back on itself or out of bounds, and once the current path is completely stuck, the programm will go back to the last cell drawn that can continue in another direction and repeat the process from there, until the entire screen is filled.

I have absolutely no idea if it's gonna work but I'll worry about that later, for now I'll just try things out and see what comes out.
