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
       
        # deixar a camera mais proxima do player
        self.zoom = 2
        tamanho_tela = self.superficie_tela.get_size()
        self.vista = pygame.Surface((tamanho_tela[0] // self.zoom, tamanho_tela[1] // self.zoom))

        #calcula o deslocamento da câmera
        self.deslocamento = pygame.math.Vector2()
        self.half_w = self.vista.get_width() // 2
        self.half_h = self.vista.get_height() // 2

        self.fundo_imagem = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.fundo_imagem.get_rect(topleft = (0,0))

    def center_target_camera(self, alvo):
        self.deslocamento.x = alvo.rect.centerx - self.half_w
        self.deslocamento.y = alvo.rect.centery - self.half_h

        #para a camera nao mostrar fora do mapa(a tela preta que estava antes)
        max_x = self.ground_rect.width - self.half_w * 2
        max_y = self.ground_rect.height - self.half_h * 2
        self.deslocamento.x = max(0,min(self.deslocamento.x, max_x))
        self.deslocamento.y = max(0,min(self.deslocamento.y, max_y))
    
    def custom_draw(self,player):

        #Limitação para o player não sair do mapa

          #sprite tem 150 de largura/dividi ele pela metade para dar o raio
        player_x = player.rect.width // 2
        player_y = player.rect.height // 2

        if player.rect.centerx - player_x < 0:
            player.rect.centerx = player_x 
        if player.rect.centerx + player_x > self.ground_rect.width:
            player.rect.centerx = self.ground_rect.width - player_x

        if player.rect.centery - player_y < 0:
            player.rect.centery = player_y 
        if player.rect.centery + player_y > self.ground_rect.height:
            player.rect.centery = self.ground_rect.height - player_y

         #centralizar no player
        self.center_target_camera(player)

        fundo_posicao = self.ground_rect.topleft - self.deslocamento
        self.vista.blit(self.fundo_imagem,fundo_posicao)

        for sprite in sorted(self.sprites(),key=lambda sprite:sprite.rect.bottom):
            posicao_tela = sprite.rect.topleft - self.deslocamento
            self.vista.blit(sprite.image,posicao_tela)

        pygame.transform.scale(self.vista, self.superficie_tela.get_size(), self.superficie_tela)



