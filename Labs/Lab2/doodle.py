from textwrap import fill
from turtle import * 
from Lab2_functions import *

def main():
    eye(100, 100, 20, "blue")
    eye(-120, 100, 20,"green")
    mouth(-110, 0)
    Screen().exitonclick()

def eye(x, y, size, color):
    fillcolor(color)
    penup()
    setposition(x, y)
    pendown()
    begin_fill()
    circle(size)
    end_fill()

def mouth(x, y):
    penup()
    setposition(x, y)
    pendown()
    
    right(90)
    circle(100, 180)

main()