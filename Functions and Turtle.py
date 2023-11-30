# Functions and Turtle
# Author : Ruby
# Date : 28th Nov 2023

import turtle

Skittles_yellow = turtle

Skittles_yellow = turtle.Turtle
Skittles_yellow.color("yellow")
Skittles_yellow.shape("turtle")

def squared(num : float) -> float : 
    """Ruturns the given number squared"""
    return num **2

for _ in range(4) :
    Skittles_yellow.forward(25)
    Skittles_yellow.left(90)
