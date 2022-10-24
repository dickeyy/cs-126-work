import turtle as t
import keyboard as k

# Define main
aim = ''

def main():
    t.setup(200, 200)
    t.speed(0)

    # when the user preses the down  button, print(down)
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

# Define me_up functionq
def me_up():
    print('up')

def me_down():
    print('down')

def me_left():
    print('left')

def me_right():
    print('right')

# Call main
main()