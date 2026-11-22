import pygame
from pygame import *
from sys import exit
from interface.scream import *
from classes.player import Player

Player=Player()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

tempo.tick(fps)
