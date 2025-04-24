from .gameobject import GameObject
import pygame
import math

bullet_speed = 10
bullet_radius = 5  # tamanho bullets
RED = (255, 0, 0)


class Projetil(GameObject):
    def __init__(self, x, y, angle):
        super().__init__("projetil")
        self.x = x
        self.y = y
        self.dx = math.cos(angle) * bullet_speed
        self.dy = math.sin(angle) * bullet_speed

    def update(self, events):
        self.x += self.dx
        self.y += self.dy
        if (
            self.x < -bullet_radius
            or self.x > self.globals.screen_size.x + bullet_radius
        ):
            self.__del__()

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), bullet_radius)
