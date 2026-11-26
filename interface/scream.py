import pygame
from constante import LARGURA,ALTURA,FPS

pygame.init()

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('marry me or dont')

tempo = pygame.time.Clock()