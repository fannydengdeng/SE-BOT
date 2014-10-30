from myro import *

MAX_SIDE = 675
MAX_CORNER = 700
NINETY = 0.799
FORTY_FIVE = 0.4
THIRTY = 0.266
K = 0


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
    while count != 7:
        sumLeft += getObstacle(side)
        count += 1
    return sumLeft/count

def turn_right():
    stop()
    rotate(-1)
    wait(NINETY+K)
    stop()

def turn_left():
    rotate(1)
    wait(NINETY)
    stop()

def turn_corner_right():
    stop()
    rotate(-1)
    wait(THIRTY+K)
    stop()

def turn_corner_left():
    stop()
    rotate(1)
    wait(THIRTY)
    stop()

def turn_right_45():
    stop()
    rotate(-1)
    wait(FORTY_FIVE+K)
    stop()

def turn_left_45():
    stop()
    rotate(1)
    wait(FORTY_FIVE)
    stop()

def move():
    motors(1, 1)
    wait(0.5)
    stop()

def right_side():
    counter = 0
    stage = 1
    while stage == 1:
        turn_right()
        move()
        counter += 1
        turn_left()
        if not obs():
            wait(0.25)
            turn_corner_left()
            if not obs_corner():
                wait(0.25)
                turn_corner_right()
                wait(0.25)
                turn_corner_right()
                if not obs_corner():
                    wait(0.25)
                    turn_corner_left()
                    stage = 2
                else:
                    turn_corner_left()
                move()
                stage = 2
            else:
                turn_corner_right()

    while counter != -2:
        move()
        counter -= 1

    turn_right_45()
    forward(1, 3)

def left_side():
    stage = 1
    counter = 0
    while stage == 1:
        turn_left()
        move()
        counter += 1
        turn_right()
        if not obs():
            wait(0.25)
            turn_corner_right()
            if not obs_corner():
                wait(0.25)
                turn_corner_left()
                wait(0.25)
                turn_corner_left()
                if not obs_corner():
                    wait(0.25)
                    turn_corner_right()
                    move()
                    stage = 2
                else:
                    turn_corner_right()
            else:
                turn_corner_left()

    while counter != -2:
        move()
        counter -= 1

    turn_left_45()
    forward(1, 3)
    stop()

init("com3")
while not obs():
    forward(1)
stop()

turn_right_45()
if not obs():
    """
    turn_left()
    left_side()
    """
    turn_left_45()
    turn_left_45()
    if not obs():
        turn_right_45()
        backward(1, 0.25)
        MAX_SIDE = 550
        MAX_CORNER = 500
        turn_left_45()
        move()
        turn_right()
        left_side()
    else:
        turn_right_45()
        turn_right_45()
        turn_left()
        right_side()
else:
    left_side()

