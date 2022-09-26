from turtle import *
from Lab2_functions import *

ORIGIN_X = -360
ORIGIN_Y = 320

def main():
    bgcolor('gray')
    hideturtle()
    speed('fastest')

    height = 650
    width = 400
    screen = Screen()
    screen.screensize(width, height)

    upper_left()
    mid_left()
    lower_left()
    lower_middle()
    lower_right()
    upper_right()

    Screen().exitonclick()

def row(count, wdith, height, x, y):
    color = 'white'
    for i in range(count):
        newX = x + (i * wdith)

        if color == 'black':
            color = 'white'
            draw_rect(newX, y, wdith, height, color)
        else:
            color = 'black'
            draw_rect(newX, y, wdith, height, color)

            # Draw a blue X
            draw_line(newX, y, newX + wdith, y + height, 'blue')
            draw_line(newX, y + height, newX + wdith, y, 'blue')

        penup()
        forward(wdith)
        pendown()
        
def upper_left():
    row(8, 20, 20, ORIGIN_X, ORIGIN_Y)

def mid_left():
    row(10, 30, 30, ORIGIN_X + 50, ORIGIN_Y - 70)

def lower_left():
    for i in range(8):
        row(8, 25, 25, ORIGIN_X, ORIGIN_Y - 250 - (i * 25))

def lower_middle():
    for i in range(6):
        if (i % 2) == 0:
            x_offset = 0
        else:
            x_offset = 10
        row(6, 25, 25, ORIGIN_X + (250 + x_offset), ORIGIN_Y - 300 - (i * 25))

def lower_right():
    for i in range(10):
        if (i % 2) == 0:
            x_offset = 0
        else:
            x_offset = 10
        row(10, 20, 20, ORIGIN_X + (500 + x_offset), ORIGIN_Y - 300 - (i * 20))

def upper_right():
    for i in range(4):
        if (i % 2) == 0:
            x_offset = 0
        else:
            x_offset = 35
        row(4, 35, 35, ORIGIN_X + (500 + x_offset), ORIGIN_Y - 50 - (i * 35))

main()