from turtle import *
# Draw a line from (x1, y1) to (x2, y2)
# Make line color
def draw_line(x1, y1, x2, y2, color):
    # Save current location and state
    # current_position = pos()
    pen_state = pen()
    # Draw line
    pencolor(color)
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)
    up()
    # Reset position, color, and state
    # goto(current_position)
    pen(pen_state)


# Draw a draw_rect with the upper left corner at x,y
# and with dimensions x_size by y_size. Use color for
# background

def draw_rect(x, y, x_size, y_size, color):
    # Save current location and state
    # current_position = pos()
    pen_state = pen()
    # Set rectangle colors
    fillcolor(color)
    pencolor(color)
    # Move Turtle to x,y without drawing a line
    up()
    goto(x,y)
    # Draw the rectangle and fill it
    down()
    setheading(90)
    begin_fill()
    forward(x_size)
    right(90)
    forward(y_size)
    right(90)
    forward(x_size)
    right(90)
    forward(y_size)
    end_fill()
    up()
    
    # Reset position, color, and state
    # goto(current_position)
    pen(pen_state)


    
