from .gameobject import GameObject
from .projetil import Projetil
import pygame
import math
from pygame import Vector2

player_radius = 20  # tamanho do player (circulo)
player_speed = 5


class Jogador(GameObject):
    def __init__(self):
        super().__init__("jogador")
        self.pos = Vector2(400, 300)
        self.health = 1

    def update(self, events):
        for event in events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
            ):  # atirar no clique esquerdo
                mouse_x, mouse_y = pygame.mouse.get_pos()  # recupera posição do mouse

                self.dx = (
                    mouse_x - self.pos[0]
                )  # daqui pra baixo calcula exatamente a posição dos eixos
                self.dy = (
                    mouse_y - self.pos[1]
                )  # em relação ao mouse, peguei da internet, não sei como funciona 100%
                # mas ele ta pegando a posicao do jogador no mapa e vendo a diferença com o mouse
                angle = math.atan2(
                    self.dy, self.dx
                )  # angulo em relaçao ao personagem e mouse

                Projetil(self.pos[0], self.pos[1], angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos[1] -= player_speed
        if keys[pygame.K_s]:
            self.pos[1] += player_speed
        if keys[pygame.K_a]:
            self.pos[0] -= player_speed
        if keys[pygame.K_d]:
            self.pos[0] += player_speed

        inimigos = GameObject.find("inimigo")
        for enemy in inimigos:
            # verifica se o projetil colidiu com o inimigo
            if (
                math.sqrt(
                    (self.pos.x - enemy.pos.x) ** 2 + (self.pos.y - enemy.pos.y) ** 2
                )
                < enemy.radius + player_radius
            ):
                enemy.__del__()
                if self.health > 0:
                    self.health -= 1
                if self.health <= 0:
                    print("Jogador morreu")
                break

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), player_radius
        )
