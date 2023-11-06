# Pumpkin Drawing
# Author:
# Date: 31 October 2023
import turtle
import time
window = turtle.Screen()
window.bgcolor("black")
# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)
# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)
# Left eye
carver.penup()
carver.setposition(-38, 20)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(20)
carver.end_fill()
carver.penup()
# Right eye
carver.penup()
carver.setposition(38, 20)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(20)
carver.end_fill()
carver.penup()
# Mouth
carver.penup()
carver.setposition(0, -10)
carver.pendown()
carver.right(90)
carver.circle(50, 120)
carver.penup()
# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)
turtle.done()









