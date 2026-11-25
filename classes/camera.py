import pygame, sys
from random import randint

#quero usar isso dps para criar uma sobreposição de arvore e sprites
    #class Tree(pygame.sprite.Sprite):
        #def __init__(self, pos, group):
            #super().__init__(group)
            #self.image = pygame.image.load('graphics/tree.png').convert_alpha()
            #self.rect = self.image.get_rect(topleft = pos)


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.superficie_tela = pygame.display.get_surface()

        #calcula o deslocamento da câmera
        self.deslocamento = pygame.math.Vector2()
        self.half_w = self.superficie_tela.get_size()[0] // 2
        self.half_h = self.superficie_tela.get_size()[1] // 2

        self.fundo_imagem = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.fundo_imagem.get_rect(topleft = (0,0))

    def center_target_camera(self, alvo):
        self.deslocamento.x = alvo.rect.centerx - self.half_w
        self.deslocamento.y = alvo.rect.centery - self.half_h
    
    def custom_draw(self,player):

        #Limitação para o player não sair do mapa

          #sprite tem 150 de largura/dividi ele pela metade para dar o raio
        player_raio = player.rect.width // 2

        if player.rect.centerx - player_raio < 0:
            player.rect.centerx = player_raio 
        if player.rect.centerx + player_raio > self.ground_rect.width:
            player.rect.centerx = self.ground_rect.width - player_raio

        if player.rect.centery - player_raio < 0:
            player.rect.centery = player_raio 
        if player.rect.centery + player_raio > self.ground_rect.height:
            player.rect.centery = self.ground_rect.height - player_raio

         #centralizar no player
        self.center_target_camera(player)

        fundo_posicao = self.ground_rect.topleft - self.deslocamento
        self.superficie_tela.blit(self.fundo_imagem,fundo_posicao)

        for sprite in sorted(self.sprites(),key=lambda sprite:sprite.rect.centery):
            posicao_tela = sprite.rect.topleft - self.deslocamento
            self.superficie_tela.blit(sprite.image,posicao_tela)


