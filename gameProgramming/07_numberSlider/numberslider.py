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
FPS = 30 # This  is maximum value! Won't make a slow computer run faster.
BLANK = None

# COLOR VALUES IN (R, G, B) format () w/ more than one value inside is a tuple
# 0 = No value for that color, 255 = maximum value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE # BACKGROUND COLOR
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # MEASURED PIXELS
