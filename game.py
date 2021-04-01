import pygame
import sys
import random

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

SCREEN_WITH = 800
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_WITH,SCREEN_HEIGHT))

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

