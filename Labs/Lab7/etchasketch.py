# Import packages
from turtle import *
import keyboard as k

# Define globals
aim = ''

# Define main
def main():
    # Set up turtle
    setworldcoordinates(0,1000,1000,0)
    pen_state = pen()
    speed(100)
    up()
    goto(500,500)
    down()
    # Run loop
    loop()

# Run loop
def loop():
    # Global aim
    global aim
    # Start loop
    while aim != 'q':
        if k.is_pressed('w'):
            me_up()
        if k.is_pressed('s'):
            me_down()
        if k.is_pressed('a'):
            me_left()
        if k.is_pressed('d'):
            me_right()
        if k.is_pressed('q'):
            aim = 'q'

# Define up
def me_up():
    pen_state = pen()
    pen_pos = list(pos())

    # Calculate if the turtle goes off screen
    if pen_pos[1] == 0:
        hideturtle()
        up()
        speed(5000)
        goto(pen_pos[0], 1000)
        down()
        speed(100)
        showturtle()

    # Move up
    setheading(270)
    forward(10)
    
def me_down():
    pen_state = pen()
    pen_pos = list(pos())

    # Calculate if the turtle goes off screen
    if pen_pos[1] == 1000:
        hideturtle()
        up()
        speed(5000)
        goto(pen_pos[0], 0)
        down()
        speed(100)
        showturtle()

    # Move down
    setheading(90)
    forward(10)

def me_left():
    pen_state = pen()
    pen_pos = list(pos())

    # Calculate if the turtle goes off screen
    if pen_pos[0] == 0:
        hideturtle()
        up()
        speed(5000)
        goto(1000, pen_pos[1])
        down()
        speed(100)
        showturtle()

    # Move left
    setheading(180)
    forward(10)

def me_right():
    pen_state = pen()
    pen_pos = list(pos())

    # Calculate if the turtle goes off screen
    if pen_pos[0] == 1000:
        hideturtle()
        up()
        speed(5000)
        goto(0, pen_pos[1])
        down()
        speed(100)
        showturtle()

    # Move right
    setheading(360)
    forward(10)

# Call main
main()
