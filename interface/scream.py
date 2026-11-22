import pygame
from constante import largura,altura,fps

pygame.init()

tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('marry me or dont')

tempo=pygame.time.Clock()