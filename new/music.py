import pygame,sys
from pygame.locals import *

pygame.init()
file = 'Pink.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()