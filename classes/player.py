import pygame
from interface.scream import tela


class Player(pygame.sprite.Sprite):
    def __init__(self, tamanho_na_tela=(150, 150)):
        super().__init__()
        self.animacoes = {                     #fiz um dicionario para guardar os frames
            "baixo":    self.extrair_frames('sprites/cavaleiro_baixo.png', colunas=8, tamanho=tamanho_na_tela),
            "parado":   self.extrair_frames('sprites/idle.png', colunas=8, tamanho=tamanho_na_tela),
            "direita":  self.extrair_frames('sprites/walk right.png', colunas=8, tamanho=tamanho_na_tela),
            "esquerda": self.extrair_frames('sprites/walk left.png', colunas=8, tamanho=tamanho_na_tela)
        }

        self.estado = "parado"
        self.atual = 0
        self.velocidade_animacao = 0.35

        self.image = self.animacoes[self.estado][int(self.atual)]
        self.rect = self.image.get_rect(topleft=(100, 100))
        self.velocidade = 5

    def extrair_frames(self, caminho, colunas, tamanho=None):
        sheet = pygame.image.load(caminho).convert_alpha()
        largura_total, altura_total = sheet.get_size()
        largura_frame = largura_total // colunas

        frames = []
        for col in range(colunas):
            rect = pygame.Rect(col * largura_frame, 0, largura_frame, altura_total)
            frame = sheet.subsurface(rect)
            
            # Padroniza o tamanho para evitar diferença,nao deu certo tem que corrigir
            if tamanho:
                frame = pygame.transform.scale(frame, tamanho)
                
            frames.append(frame)
        return frames

    def update(self):  #movimentação do player
        teclas = pygame.key.get_pressed()
        novo_estado = "parado"

        if teclas[pygame.K_s]:
            self.rect.y += self.velocidade
            novo_estado = "baixo"
        elif teclas[pygame.K_w]:
            self.rect.y -= self.velocidade
            novo_estado = "baixo"

        if teclas[pygame.K_d]:
            self.rect.x += self.velocidade
            novo_estado = "direita"
        elif teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
            novo_estado = "esquerda"

        if novo_estado != self.estado:  #verifica se mudou de direção e reinicia a animação
            self.estado = novo_estado
            self.atual = 0

        frames_atuais = self.animacoes[self.estado]   #loop da animação
        self.atual += self.velocidade_animacao
        if self.atual >= len(frames_atuais):
            self.atual = 0

        self.image = frames_atuais[int(self.atual)]
