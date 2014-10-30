__author__ = 'fannydeng'

from myro import *
from random import *
import Image
from pygame import *
import numpy as np

def main():

    pygame.init()
    win = pygame.display.set_mode((600,400), 0, 32)
    win.fill((255, 255, 255))
    pygame.display.set_caption('Colour Detection')
    pygame.mouse.set_visible(1)
    pygame.display.flip()

    uploadButton = pygame.draw.rect (win, (0,0,0), (50, 75, 225, 50), 2)
    pygame.display.update()

    buttonFont = pygame.font.SysFont('Calibri', 15)
    titleFont = pygame.font.SysFont('Calibri', 25)
    labelTitle = titleFont.render('Colour Detection Program', 1, (0,0,0))
    labelUploadButton = buttonFont.render ('Click Here to Import a Picture', 1, (0,0,0))
    win.blit(labelTitle, (150, 25))
    b = win.blit(labelUploadButton, (75, 90))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b.collidepoint(event.pos):
                    analyze()
                else:
                    pass
            else:
                pass

            if event.type == pygame.QUIT:
                pygame.quit()

def analyze():
    '''colourList = ['black', 0,0,0
                  'darkGray', 64,64,64
                  'gray', 128,128,128
                  'lightGray', 192,192,192
                  'white', 255,255,255
                  'red', 255,0,0
                  'lime', 0,255,0
                  'blue', 0,0,255
                  'yellow', 255,255,0
                  'magenta', 255,0,255
                  'cyan', 0,255,255
                  'maroon', 128,0,0
                  'green', 0,128,0
                  'navy', 0,0,128
                  'olive', 128,128,0
                  'purple', 128,0,128
                  'teal'] 0,128,128'''

    colourCount = [0]*17

    image = Image.open(pickAFile()) #closing import window without importing quits the program)
    width, height = image.size
    pixel = image.load()
    i=1
    j=1

    while i < width:
        while j < height:
            r, g, b = pixel[i,j]
            if np.abs(r-g) <= 32 and np.abs(g-b) <= 32 and np.abs(r-b) <= 32:
                avg3 = (r+g+b)/3
                if avg3 < 32:
                    colourCount[0]+=1
                elif avg3 >= 32 and avg3 < 96:
                    colourCount[1]+=1
                elif avg3 >= 96 and avg3 < 160:
                    colourCount[2]+=1
                elif avg3 >= 160 and avg3 < 224:
                    colourCount[3]+=1
                else:
                    colourCount[4]+=1
            elif np.abs(g-b) < 32:
                if r < 192:
                    colourCount[11]+=1
                else:
                    colourCount[5]+=1
            elif np.abs(r-b) < 32:
                if g < 192:
                    colourCount[12]+=1
                else:
                    colourCount[6]+=1
            elif np.abs(r-g) < 32:
                if b < 192:
                    colourCount[13]+=1
                else:
                    colourCount[7]+=1
            elif r <= 32:
                avg2 = (g+b)/2
                if avg2 < 192:
                    colourCount[16]+=1
                else:
                    colourCount[10]+=1
            elif g <= 32:
                avg2 = (r+b)/2
                if avg2 < 192:
                    colourCount[15]+=1
                else:
                    colourCount[9]+=1
            elif b <= 32:
                avg2 = (r+g)/2
                if avg2 < 192:
                    colourCount[14]+=1
                else:
                    colourCount[8]+=1
            j+=1
        i+=1

    mostFreq = 0
    k = 0
    while k < 17:
        if colourCount[k] > mostFreq:
            mostFreq = k
        k+=1

    if mostFreq == 0:
        colour = 'Black'
    elif mostFreq == 1:
        colour = 'Dark Gray'
    elif mostFreq == 2:
        colour = 'Gray'
    elif mostFreq == 3:
        colour = 'Light Gray'
    elif mostFreq == 4:
        colour = 'White'
    elif mostFreq == 5:
        colour = 'Red'
    elif mostFreq == 6:
        colour = 'Lime'
    elif mostFreq == 7:
        colour = 'Blue'
    elif mostFreq == 8:
        colour = 'Yellow'
    elif mostFreq == 9:
        colour = 'Magenta'
    elif mostFreq == 10:
        colour = 'Cyan'
    elif mostFreq == 11:
        colour = 'Maroon'
    elif mostFreq == 12:
        colour = 'Green'
    elif mostFreq == 13:
        colour = 'Navy'
    elif mostFreq == 14:
        colour = 'Olive'
    elif mostFreq == 15:
        colour = 'Purple'
    elif mostFreq == 16:
        colour = 'Teal'
    else:
        colour = 'Unidentified'
    print (colour)
    return colour

    # pink      = makeColor(255, 175, 175)

main()