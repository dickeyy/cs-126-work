from turtle import *
import keyboard as k

aim = ''

def main():
    setworldcoordinates(0,1000,1000,0)
    pen_state = pen()
    up()
    goto(500,500)
    down()
    idk()
    
def idk():
    global aim
    while aim != "q":
        key_press = get_key()
       
def get_key():
    if k.is_pressed('w'):
        me_up()
    elif k.is_pressed('s'):
        me_down()
    elif k.is_pressed('a'):
        me_left()
    elif k.is_pressed('d'):
        me_right()
    elif k.is_pressed('q'):
        global aim
        aim = 'q'
def me_up():
    pen_state = pen()

    setheading(0)
    forward(1)
    
def me_down():
    pen_state = pen()

    setheading(180)
    forward(1)

def me_left():
    pen_state = pen()

    setheading(360)
    forward(1)

def me_right():
    pen_state = pen()

    setheading(90)
    forward(1)
    

main()
