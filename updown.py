import turtle

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

def up():
    global direction
    direction=UP
    print('you pressed up')
    return direction

def down():
    global direction
    direction=DOWN
    print('you pressed down')
    return direction

def left():
    global direction
    direction=LEFT
    print('you pressed left')
    return direction

def right():
    global direction
    direction=RIGHT
    print('you pressed right')
    return direction 

turtle.mainloop()






