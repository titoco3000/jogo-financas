from .gameobject import GameObject, globals
import pygame
import math

bullet_speed = 10
bullet_radius = 5  # tamanho bullets
RED = (255, 0, 0)


class Projetil(GameObject):
    som_colisao = None
    som_morte_inimigo = None

    def __init__(self, x, y, angle):
        super().__init__("projetil")
        self.x = x
        self.y = y
        self.dx = math.cos(angle) * bullet_speed
        self.dy = math.sin(angle) * bullet_speed

        # Carregar sons se ainda não estiverem carregados
        if Projetil.som_colisao is None:
            Projetil.som_colisao = pygame.mixer.Sound("sons/colisao-projetil.wav")
            Projetil.som_colisao.set_volume(0.7)

        if Projetil.som_morte_inimigo is None:
            Projetil.som_morte_inimigo = pygame.mixer.Sound("sons/morte-inimigo.wav")
            Projetil.som_morte_inimigo.set_volume(1.0)

    def update(self, events):
        self.x += self.dx
        self.y += self.dy

        if (
            self.x < -bullet_radius
            or self.x > globals.var.screen_size.x + bullet_radius
        ):
            self.__del__()
        else:
            inimigos = GameObject.find("inimigo")
            for enemy in inimigos:
                distancia = math.hypot(self.x - enemy.pos.x, self.y - enemy.pos.y)
                if distancia < enemy.radius + bullet_radius:
                    self.__del__()

                    # Toca som de colisão com inimigo
                    Projetil.som_colisao.play()

                    enemy.health -= 1
                    if enemy.health <= 0:
                        # Toca som de morte do inimigo
                        Projetil.som_morte_inimigo.play()
                        enemy.__del__()
                    break

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), bullet_radius)
