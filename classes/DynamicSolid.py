import pygame

class DynamicSolid:  # NOTA: por enquanto só funciona colisões dinamico -> estatico, e não dinamico -> dinamico
                     # (a não ser que você trate um dos sólidos como estatico)


    def __init__(self, left: int, top: int, width: int, height: int):
        self.hitbox = pygame.Rect(left, top, width, height)
        self.velocity = pygame.Vector2(0, 0)

    def force_move(self, x: int, y: int):
        self.hitbox = self.hitbox.move(x, y)

    def update(self, dt: float): # atualiza a posição baseado em dt e a velocidade
        self.hitbox.x += self.velocity.x * dt
        self.hitbox.y += self.velocity.y * dt

    def unclip(self, rect: pygame.Rect):

        if self.velocity.x != 0: # transforma uma das componentes da velocidade em 1
            dx = self.velocity.x / abs(self.velocity.x)
            dy = self.velocity.y / abs(self.velocity.x)
        elif self.velocity.y != 0:
            dx = self.velocity.x / abs(self.velocity.y)
            dy = self.velocity.y / abs(self.velocity.y)
        else:
            return # se as duas componentes forem 0, espera uma próxima chamada válida

        back_x = back_y = 0 # contagem separada para manter a precisão do float

        while rect.colliderect(self.hitbox.move(back_x, back_y)): # regride o movimento até não colidir
            back_x -= dx
            back_y -= dy

        if (rect.colliderect(self.hitbox.move(back_x - 1, back_y)) or
            rect.colliderect(self.hitbox.move(back_x + 1, back_y))): # move um pixel para cada lado para manter uma das componentes
            self.hitbox = self.hitbox.move(back_x, 0)                # da velocidade
        elif (rect.colliderect(self.hitbox.move(back_x, back_y - 1)) or
            rect.colliderect(self.hitbox.move(back_x, back_y + 1))):
            self.hitbox = self.hitbox.move(0, back_y)
        else:
            self.hitbox = self.hitbox.move(back_x, back_y) # caso de colisão de canto

    def unclip_list(self, rect_list : list):  # aplica unclip a uma série de objetos sólidos
        while self.hitbox.collidelist(rect_list) != -1:
            self.unclip(rect_list[self.hitbox.collidelist(rect_list)])
