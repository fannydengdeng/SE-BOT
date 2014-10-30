from myro import *

MAX_SIDE = 1050
MAX_CORNER = 800

def obs():
    if  check(1) > MAX_SIDE:
        return True
    elif check(0) > MAX_SIDE-150:
        return True
    elif check(2) > MAX_SIDE-150:
        return True
    return False

def obs_corner():
    if  check(1) > MAX_CORNER:
        return True
    elif check(0) > MAX_CORNER-50:
        return True
    elif check(2) > MAX_CORNER-50:
        return True
    return False

def check(side):
    sumLeft = 0
    count = 0
    while count != 5:
        sumLeft += getObstacle(side)
        count += 1
    return sumLeft/count

def turn_right():
    stop()
    rotate(-1)
    wait(0.807)
    stop()

def turn_left():
    stop()
    rotate(1)
    wait(0.799)
    stop()

def turn_corner_right():
    stop()
    rotate(-1)
    wait(0.266)
    stop()

def turn_corner_left():
    stop()
    rotate(1)
    wait(0.265)
    stop()

def move():
    motors(1, 1)
    wait(0.5)
    stop()

init("com3")
stage = 0
counter = 0
while not obs():
    move()
stop()
stage = 1
while stage == 1:
    turn_left()
    counter += 1
    move()
    turn_right()
    if not obs():
        turn_corner_right()
        if not obs():
            wait(0.25)
            turn_corner_left()
            move()
            stage = 2
        else:
            turn_corner_left()

while stage == 2:
    move()
    turn_right()
    if not obs():
        turn_corner_right()
        if not obs_corner():
            wait(0.25)
            turn_corner_left()
            wait(0.25)
            turn_corner_left()
            if not obs_corner():
                turn_corner_right()
                stage = 3
            else:
                turn_corner_right()
                turn_left()
        else:
            turn_corner_left()
            turn_left()
    else:
        turn_left()

while stage == 3:
    if counter != -1:
        move()
        counter -= 1
    else:
        stage = 4

turn_left()
forward(1, 3)
stop()