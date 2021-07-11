# install and import the required modules
from turtle import *
from random import randint

# using the normal shape for turtle
speed(0)
penup()
goto(-140, 140)

# race track for turtles
for step in range(15):
    write(step, align='center')
    right(90)

    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)

    penup()
    backward(160)
    left(90)
    forward(20)

# first turtle details
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# first turtle going to race track
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# 360 degree turn on right side
for turn in range(10):
    player_1.right(36)

# second turtle details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# second turtle going to race track
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# 360 degree turn on left side
for turn in range(72):
    player_2.left(5)

# third turtle details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# third turtle going to race track
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# 360 degree turn on right side
for turn in range(60):
    player_3.right(6)

# fourth turtle details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# fourth turtle going to race track
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# 360 degree turn on left side
for turn in range(30):
    player_4.left(12)

# turtles running at random speeds
for turn in range(100):
    player_1.forward(randint(1, 6))
    player_2.forward(randint(1, 6))
    player_3.forward(randint(1, 6))
    player_4.forward(randint(1, 6))
