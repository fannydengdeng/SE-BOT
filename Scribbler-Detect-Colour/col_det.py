import PIL
from myro import *

def most_col(image):
    w, h = image.size
    colours = image.getcolors(w * h)

    max = colours[0][0]
    index = 0

    for i in range(0, len(colours)):
        if colours[i][0] > max:
            max = colours[i][0]
            index = i

    return colours[index]

init("com3")
max_r = 0
max_g = 0
max_b = 0
min_r = 255
min_g = 255
min_b = 255

for i in range(0, 5):
    picture = takePicture("color")
    savePicture(picture, "test.jpg")
    print "Picture taken"
    image = PIL.Image.open("test.jpg")
    col = most_col(image)
    if col[1][0] > max_r:
        max_r = col[1][0]
    elif col[1][0] < min_r:
        min_r = col[1][0]
    if col[1][1] > max_g:
        max_b = col[1][1]
    elif col[1][1] < min_g:
        min_b = col[1][1]
    if col[1][2] > max_b:
        max_b = col[1][2]
    elif col[1][2] < min_b:
        min_b = col[1][2]

print "(" + min_r + ", " + max_r + ")"
print "(" + min_g + ", " + max_g + ")"
print "(" + min_b + ", " + max_b + ")"