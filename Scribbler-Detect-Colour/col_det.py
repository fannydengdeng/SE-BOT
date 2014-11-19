from PIL import Image

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