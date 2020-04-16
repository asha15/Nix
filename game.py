import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100, 100] 
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/c.png")

while 1:
    #clearing the screen
    screen.fill(0)

    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    #drawing the screen elements
    screen.blit(player, playerpos)
    #update the screen
    pygame.display.flip()
    #looping throught events
    for event in pygame.event.get():
        #check if the event is the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_LEFT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_RIGHT:
                keys[1] = False
            elif event.key == pygame.k_DOWN:
                keys[2] = False
            elif event.key == pygame.K_LEFT:
                keys[3] = False

    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5






















