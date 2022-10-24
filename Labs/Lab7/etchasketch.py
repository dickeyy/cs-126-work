import turtle as t
import keyboard as k

# Define main
def main():
    # Set up turtle
    t.setup(400, 400)
    t.speed(0)

    # call etchasketch function
    etchasketch()

# Define etchasketch function
def etchasketch():
    # Set up turtle
    t.pensize(5)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Set up keyboard
    k.on_press_key("up", up)
    k.on_press_key("down", down)
    k.on_press_key("left", left)
    k.on_press_key("right", right)
    k.on_press_key("space", space)
    k.on_press_key("c", c)
    k.wait("esc")

# Define up function
def up():
    t.setheading(90)
    t.forward(10)

# Define down function  
def down():
    t.setheading(270)
    t.forward(10)

# Define left function
def left():
    t.setheading(180)
    t.forward(10)

# Define right function
def right():
    t.setheading(0)
    t.forward(10)

# Define space function
def space():
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Define c function
def c():
    t.clear()

# Call main
main()