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

