# Number slider, Jermya Goodwine, based on a project by Al Sweigart, v0.0

import sys, random, pygame
# sys module provides access to system resources such (i.e. Operating System Commands.)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of mudule.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for the game board
BOARDWIDTH = 4 # COLUMNS
BOARDHIEGHT = 4 # ROW
TILESIZE = 80 # WHAT UNIT DO YOU THINK THIS IS? PIXELS DUH.
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 
BLANK = None