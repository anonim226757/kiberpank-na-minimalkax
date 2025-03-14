print (1)
import os
import pygme
import random
from pygame  import *

pygame.init()

scr_size = (width,height) = (600,150)
FPS = 60
gravity = 0.6

black = (0,0,0)
white = (255,255,255)
background_col =(235,235,235)

high_score = 0

screen =pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption ("диназавррар")

jamp_sound = pygame.mixer.Sound('sprintes/jump.wav')
die_sound = pygame.mixer.Sound('sprintes/jump.wav')
checkPoint_sound = pygame.mixer.Sound('sprintes/jump.wav')

def load_image(
    name
    sizex=-1,
    sizey=-1
    colorkey=None'
):

    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is -1:
        colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, RLEACCEL)

  is sizex != -1 sizey != -1:
    image = pygame.transfrom.scale(image, (sizex, sizey))

    return (image, image.get_rect())
 
def  load_sprite_rect(
        sheetname,
        nx,
        ny,
        skalex = -1,
        skaley = -1,
        colorkey = None
    ):
    fullname = os.path.join('sprites', sheetname)
    sheet = pygame.image
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i range(0,ny)
        for j  in range(0, nx)
            rect = pygame.Rect((j*sizey, sizex, sizey))
            image =  pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0), rect)

            if colorkey is not None:
                if colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey, RLEACCEL)

            if scalex != -1 or scaley != -1:
                imge = pygame.transform.scale(image,(scalex, scaley))

            sprites.append (image)

        sprite_rect = sprintes[0].get_rect

    def disp_gameOver_msg(retbuton_image,gameover_image):
       retbutton_rect = retbuton_image.get_rect()
       retbutton_rect.ceterx = width / 2
       retbutton_rect.top = height*0.52

       gameover_rect = gaameover_image.get_rect()
       gameover_rect.centex = width / 2
       gameover_rect.centex = height*0.35

       screen.blit(retbutton_imaage,retbutton_rect)
       screen.blit(gaameover_image, gameover_rect)

    def extractDigits(number):
        if number > -1:
            digits = []
            1 = 0
            while(number/10 != 0)
            digits.append(number%10)
            number = int(number/10)

        digits.append(number%10)
        
