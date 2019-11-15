import pygame as pg
from settings import *

#################
# Define colors #
#################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#################
# Game Settings #
#################
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Eeppinen RPG"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

###### Player Settings #######

PLAYER_SPEED = 125
PLAYER_IMG = ''