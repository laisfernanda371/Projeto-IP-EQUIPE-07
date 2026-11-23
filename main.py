import pygame
from pygame import *
from sys import exit
from interface.scream import *
from classes.player import Player

pygame.init()

todas_sprites=pygame.sprite.Group()
player= Player(tamanho_na_tela=(150, 150))
todas_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    tela.fill((0,0,0))
    todas_sprites.draw(tela)
    todas_sprites.update()
    
    pygame.display.update()
    tempo.tick(fps)
