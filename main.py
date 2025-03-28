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
        def draw(self):
        screen.blit(self.image,self.rect)

    def checkbounds(self):
        if self.rect.bottom > int(0.98*height):
            self.rect.bottom = int(0.98*height)
            self.isJumping = False

    def update(self):
        if self.isJumping:
            self.movement[1] = self.movement[1] + gravity

        if self.isJumping:
            self.index = 0
        elif self.isBlinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1)%2
            else:
                if self.counter % 20 == 19:
                    self.index = (self.index + 1)%2

        elif self.isDucking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2 + 2

        if self.isDead:
           self.index = 4

        if not self.isDucking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            self.image = self.images1[(self.index)%2]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)
        self.checkbounds()

        if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1)
 class Cactus(pygame.sprite.Sprite):
            def __init__(self,speed=5,sizex=1,sizey=1):   
                pygame.sprite.Sprite.__init__(selft,self.containers)
                self.images,self.rect =loand_sprite_sheet('cacti-small.png',3,1,sizex,sizey,-1)
                self.rect.bottom = int(0.95*height)
                self.rect.left = width + self.rect.width
                self.image = self.images[random.randrange(0,3)]
                self.movement = [-1*speed,0]

            def draw(self):
                screen.blit(self.image,self.rect)

            def update(self):
                self.rect = self.rect.move(self.movement)

                if self.rect.right < 0:
                    self.kill()

        class Ptera(pygame.sprite.Sprite):
            def __init__(self,speed=5,sizex=1,sizey=1):
                pygame.sprite.Sprite.__init__(self,self.containers)
                self.images,self.rect = loand_sprite_sheet('ptera.png',2,1,sizex,sizey,-1)
                self.ptera_height = [height*0.82,height*0.75,heigth*0.60]
                self.rect.centery = self.ptera_height[random.randrange(0,3)]
                self.rect.left = width + self.rect.width
                self.image = self.images[0]
                self.movement = [-1*speed,0]
                self.index = 0
                self.counter = 0

            def draw(self) 
                screen.blit(self.image,self.rect)

            def update(self):
                if self.counter % 10 == 0:
                    self.index = (self.index+1)%2
                self.image = self.images[self.index]
                self.rect = self.rect.move(self.movement)
                self.counter = (self.counter + 1)
                if self.rect.right < 0:
                    self.kill()


        class Ground():
            def __init__(self,speed=-5):
               self.image,self.rect = loand_image(('ground.png',-1, -1,-1))
                self.image,self.rect1 = loand_image(('ground.png',-1, -1,-1))
                

    