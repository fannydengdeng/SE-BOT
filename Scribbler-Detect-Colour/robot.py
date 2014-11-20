from myro import *
from PIL import Image
from col_det import most_col
from obj_det import ObjDet
from timer import Timer
import globals
import sys

'''brown_min = (30, 10, 0)
brown_max = (36, 16, 3)
white_min = (45, 30, 0)
white_max = (76, 68, 3)
red_min = (39, 0, 0)
red_max = (255, 20, 3)'''

brown_r = (25, 40)
brown_g = (10, 18)
brown_b = (0, 63)

yellow_r = (49, 80)
yellow_g = (31, 53)
yellow_b = (0, 63)

red_r = (41, 255)
red_g = (0, 31)
red_b = (0, 63)

def turn_right():
    stop()
    rotate(-0.2)
    wait(4.82)
    stop()

def turn_left():
    stop()
    rotate(0.2)
    wait(4.81)
    stop()

def test_colour(colour):
    picture = takePicture("color")
    savePicture(picture, "test.jpg")
    print "Picture taken"
    image = Image.open("test.jpg")
    col = most_col(image)
    print col

    if colour.lower() == "brown":
        if brown_r[0] <= col[1][0] <= brown_r[1] \
                and brown_g[0] <= col[1][1] <= brown_g[1] \
                and brown_b[0] <= col[1][2] <= brown_b[1]:
            return True
    elif colour.lower() == "red":
        if red_r[0] <= col[1][0] <= red_r[1] \
                and red_g[0] <= col[1][1] <= red_g[1] \
                and red_b[0] <= col[1][2] <= red_b[1]:
            return True
    elif colour.lower() == "yellow":
        if yellow_r[0] <= col[1][0] <= yellow_r[1] \
                and brown_g[0] <= col[1][1] <= yellow_g[1] \
                and yellow_b[0] <= col[1][2] <= yellow_b[1]:
            return True
    return False

def search():
    turn_left()
    motors(0.25, 0.25)
    wait(1.75)
    turn_right()

init("com3")
globals.init()

colour = raw_input("Enter what colour to find: ")

objDetThread = ObjDet()
objDetThread.start()
timerThread = Timer()
timerThread.start()
setLEDFront(1)

while not objDetThread.obs_found:
    motors(0.25, 0.25)
    globals.time_y += 1

stop()

if test_colour(colour):
    beep(0.5, 880)
    while not globals.time_y == 0:
        motors(-0.25, -0.25)
        globals.time_y -= 1
    stop()

else:
    turn_left()
    motors(0.25, 0.25)
    wait(9)
    stop()
    turn_right()
    motors(0.25, 0.25)
    wait(6)
    stop()
    turn_right()
    while not objDetThread.obs_found:
        motors(0.25, 0.25)
        globals.time_x += 1
    stop()

    while not test_colour(colour):
        search()
        globals.time_y += 1
        if globals.times_up:
            stop()
            print "Can't find colour"
            sys.exit()
        '''while not objDetThread.obs_found:
            search()
            globals.time_y += 1'''

    beep(0.5, 880)
    turn_right()
    turn_right()
    while not globals.time_x == 0:
        motors(0.25, 0.25)
        globals.time_x -= 1
    stop()
    turn_left()
    motors(0.25, 0.25)
    wait(6)
    stop()
    while not globals.time_y == 0:
        motors(0.25, 0.25)
        globals.time_y -= 1
    stop()
    turn_left()
    motors(0.25, 0.25)
    wait(11.5)
    stop()
    setLEDFront(0)