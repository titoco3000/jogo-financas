from .gameobject import GameObject
import src.globals as globals
from . import efeitos
import pygame
from pygame import Vector2
import math

bullet_speed = 10
bullet_radius = 10  # tamanho bullets
COLOR = (242, 62, 3)


class Projetil(GameObject):
    def __init__(self, x, y, angle):
        super().__init__("projetil")
        self.x = x
        self.y = y
        self.angle = angle
        self.dx = math.cos(angle) * bullet_speed
        self.dy = math.sin(angle) * bullet_speed

        self.steps_in_direction = 2
        self.alt_direction = 1

        font = pygame.font.SysFont(None, 24)
        self.sifrao = font.render("$", True, (255, 255, 255))

    def update(self, events):
        if globals.efeitos_no_jogador.has(efeitos.ZigZagProjetil):
            self.steps_in_direction = self.steps_in_direction % 10 + 1
            if self.steps_in_direction == 1:
                self.alt_direction *= -1
                self.dx = math.cos(self.angle + 0.5 * self.alt_direction) * bullet_speed
                self.dy = math.sin(self.angle + 0.5 * self.alt_direction) * bullet_speed

            self.x += 1.2 * self.dx
            self.y += 1.2 * self.dy
        else:
            self.x += self.dx
            self.y += self.dy
        if self.x < -bullet_radius or self.x > globals.screen_size.x + bullet_radius:
            self.__del__()
        else:
            # obtem uma lista de todos os inimigos
            inimigos = GameObject.find("inimigo")

            bullet_center = Vector2(self.x, self.y)

            for enemy in inimigos:
                enemy_rect = pygame.Rect(
                    enemy.pos.x, enemy.pos.y, enemy.dimension.x, enemy.dimension.y
                )

                closest_x = max(enemy_rect.left, min(bullet_center.x, enemy_rect.right))
                closest_y = max(enemy_rect.top, min(bullet_center.y, enemy_rect.bottom))
                closest_point = Vector2(closest_x, closest_y)

                if (closest_point - bullet_center).length() < bullet_radius:
                    enemy.hit()
                    self.__del__()  # remover bullet colidido
                    break

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR, (int(self.x), int(self.y)), bullet_radius)
        screen.blit(
            self.sifrao,
            (
                int(self.x - self.sifrao.get_width() / 2),
                int(self.y - self.sifrao.get_height() / 2),
            ),
        )
