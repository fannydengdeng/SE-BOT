from myro import *
from PIL import Image
from col_det import most_col
from obj_det import ObjDet

brown_min = (30, 10, 0)
brown_max = (36, 16, 3)
white_min = (45, 30, 0)
white_max = (76, 68, 3)
red_min = (39, 0, 0)
red_max = (255, 20, 3)

brown_r = (30, 37)
brown_g = (10, 17)
brown_b = (0, 4)

white_r = (45, 76)
white_g = (30, 69)
white_b = (0, 4)

red_r = (39, 255)
red_g = (0, 21)
red_b = (0, 4)

def turn_right():
    stop()
    rotate(-1)
    wait(0.807)
    stop()

def turn_left():
    stop()
    rotate(1)
    wait(0.807)
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

def test_colour(colour):
    picture = takePicture("color")
    savePicture(picture, "test.jpg")
    print "Picture taken"
    image = Image.open("test.jpg")
    col = most_col(image)
    print col

    if colour.lower() == "brown":
        if col[1][0] in range(brown_r[0], brown_r[1]) \
                and col[1][1] in range(brown_g[0], brown_g[1]) \
                and col[1][2] in range(brown_b[0], brown_b[1]):
            return True
    elif colour.lower() == "red":
        if col[1][0] in range(red_r[0], red_r[1]) \
                and col[1][1] in range(red_g[0], red_g[1]) \
                and col[1][2] in range(red_b[0], red_b[1]):
            return True
    elif colour.lower() == "white":
        if col[1][0] in range(white_r[0], white_r[1]) \
                and col[1][1] in range(white_g[0], white_g[1]) \
                and col[1][2] in range(white_b[0], white_b[1]):
            return True
    return False

init("com3")

colour = raw_input("Enter what colour to find: ")

objDetThread = ObjDet()
objDetThread.start()

while not objDetThread.obs_found:
    motors(0.25, 0.25)

stop()

if test_colour(colour):
    beep(0.5, 880)
else:
    turn_left()
    motors(0.5, 0.5)
    wait(4)
    stop()
    turn_right()
    motors(0.25, 0.25)
    wait(3)
    turn_right()
    motors(0.5, 0.5)
    wait(1)
    stop()
    while not objDetThread.obs_found:
        motors(0.25, 0.25)
    stop()