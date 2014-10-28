__author__ = 'fannydeng'

from myro import *
from random import *
from PIL import *
from pygame import *
from pyTTS import *

class Button(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((255, 255, 255))
        pygame.display.update()

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (0, 0, 0), (175, 75, 200, 100), 2)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Upload a Photo', True, (255,0,0)), (200, 100))
        pygame.display.update()

    def __del__(self):
        if Button:
            del self

def main():

    pygame.init()
    win = pygame.display.set_mode((500, 100))
    pygame.display.set_caption('Colour Detection')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(win.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # text = makeText("Scribbler Colour Detection Program", 1)
    # textpos = text.get_rect(centerx=background.get_width()/2)
    # background.blit(text, textpos)

    if __name__ == '__main__':
        uploadButton = Button()
        uploadButton.addRect()
        uploadButton.addText()
        while True:
           for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit();
    # uploadPic = makePicture(pickAFile())
    # analyze(testPic)

def analyze(file):
    image = Image.open(file)
    pix = image.load()
    for i in (getWidth(image)):
        for j in (getHeight(image)):
            r, g, b = image.getPixel(i, j)

# black     = makeColor(  0,   0,   0)
# white     = makeColor(255, 255, 255)
# blue      = makeColor(  0,   0, 255)
# red       = makeColor(255,   0,   0)
# green     = makeColor(  0, 255,   0)
# gray      = makeColor(128, 128, 128)
# darkGray  = makeColor( 64,  64,  64)
# lightGray = makeColor(192, 192, 192)
# yellow    = makeColor(255, 255,   0)
# pink      = makeColor(255, 175, 175)
# magenta   = makeColor(255,   0, 255)
# cyan      = makeColor(  0, 255, 255)

main()