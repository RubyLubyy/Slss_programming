# Functions and Turtle
# Author : Ruby
# Date : 28th Nov 2023

import turtle

Skittles_yellow = turtle

Skittles_yellow = turtle.Turtle
Skittles_yellow.color("lightgreen")
Skittles_yellow.shape("turtle")

def squared(num : float) -> float : 
    """Ruturns the given number squared"""
    return num **2

def draw_square(side_length: float) -> None:
    for _ in range(4) :
        Skittles_yellow.forward(side_length)
        Skittles_yellow.left(90)

def draw_tree(level : int, height : int) -> None : 
    """ A recursive function that draws a tree with inital given height
    
    Params : 
    level - number representing levels of branches
    height - height of the main trunk in pixels """

    if level > 0 : 
        # 1. Draw the branch
        Skittles_yellow.forward(height)

        # 2. Turn to the left
        Skittles_yellow.left(39)

        # 3. Draw a smaller tree (current level -1)
        draw_tree(level-1, height/1.5)

        # 4. Turn to the right
        Skittles_yellow.right(39 * 2)

        # 5. Drawa smaller tree (current level -1)
        draw_tree(level - 1, height / 1.5)

        # 6. Move back to the beginning
        Skittles_yellow.left(39)
        Skittles_yellow.back(height)
    else : 
        # create a level 0 tree, which is a leaf
            original_colour = Skittles_yellow.color()
            Skittles_yellow.color("green")
            Skittles_yellow.stamp()
            Skittles_yellow.color(original_colour[0])

# Setting Skittles to draw the tree
# Skittles_yellow.hideturtle()
Skittles_yellow. setheading(90)
Skittles_yellow. width(4)
Skittles_yellow.color("brown")
Skittles_yellow.shape("arrow")
Skittles_yellow.speed(200)

draw_tree(10, 150)

turtle.done()