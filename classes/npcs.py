import pygame
from interface.scream import tela

pygame.init()

class Casaveis(pygame.sprite.Sprite):
    def __init__(self, nome, sprite,posicao):
        super().__init__()

        self.nome = nome
        self.image = pygame.image.load(sprite).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=posicao)
