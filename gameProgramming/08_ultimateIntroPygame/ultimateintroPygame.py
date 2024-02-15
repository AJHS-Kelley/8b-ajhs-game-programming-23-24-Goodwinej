# jermya goodwine, Introduction to pygame, v0.0
import pygame
from sys import exit
# Almost finished, please get the last few tutorial videos completed. 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultpy/sky.jpg')
ground_surface = pygame.image.load('img/ultpy/ground.jpg')
text_surface = test_font.render("my game", False, 'Green')

# Exampe 'graphics/picture.jpg'
# Our version: 'img/ultpy/r.jpg'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything            
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)

   
