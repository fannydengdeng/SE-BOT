from myro import *

def obs():
    if  check(1) > 1050:
        return True
    elif check(0) > 900:
        return True
    elif check(2) > 900:
        return True
    return False

def obs_corner():
    if  check(1) > 800:
        return True
    elif check(0) > 850:
        return True
    elif check(2) > 800:
        return True
    return False

def check(side):
    sumLeft = 0
    count = 0
    while count != 12:
        sumLeft += getObstacle(side)
        count += 1
    return sumLeft/count

def turn_right():
    stop()
    motors(1,-1)
    wait(0.797)
    stop()

def turn_left():
    stop()
    motors(-1,1)
    wait(0.797)
    stop()

def turn_corner_right():
    stop()
    motors(1,-1)
    wait(0.2657)
    stop()

def turn_corner_left():
    stop()
    motors(-1,1)
    wait(0.2657)
    stop()

def move():
    motors(1, 1)
    wait(0.5)
    stop()

init("com3")
stage = 0
counter = 0
while not obs():
    motors(0.75, 0.75)
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
move()
move()
move()
stop()