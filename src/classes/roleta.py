from .gameobject import GameObject, globals
from .animation import Animation
import pygame
from pygame import Vector2
import math


def pie_piece(surface, pos: Vector2, raio, cor, inicio, fim):
    p = [pos]
    for n in range(inicio, fim):
        x = pos.x + int(raio * math.cos(n * math.pi / 180))
        y = pos.y + int(raio * math.sin(n * math.pi / 180))
        p.append(Vector2(x, y))
    p.append(pos)

    if len(p) > 2:
        pygame.draw.polygon(surface, cor, p)


ANIMACAO_GIRO = [
    (0, 1),
    (-10, 0.5),
    (-12, 0.3),
    (-10, 0.3),
    (360, 4),
]


class Roleta(GameObject):
    def __init__(self, pos, radius):
        super().__init__("roleta")
        self.surface_roleta = pygame.Surface(
            (2 * radius, 2 * radius), pygame.SRCALPHA, 32
        )

        fatias = 10
        cores = [
            pygame.color.THECOLORS["red"],
            pygame.color.THECOLORS["blue"],
            pygame.color.THECOLORS["green"],
            pygame.color.THECOLORS["yellow"],
            pygame.color.THECOLORS["pink"],
        ] * 2

        largura_fatia = int(360 / fatias)
        for fatia in range(fatias):
            pie_piece(
                self.surface_roleta,
                Vector2(radius, radius),
                radius,
                cores[fatia],
                fatia * largura_fatia,
                math.ceil((fatia + 1) * largura_fatia) + 1,
            )

        self.pos = pos
        self.radius = radius
        self.angulo = 0

        self.anim = Animation(ANIMACAO_GIRO)
        self.rodar()

    def rodar(self):
        self.anim.reset()
        self.anim.play()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.rodar()

        if self.anim.playing:
            self.angulo = self.anim.get_state()
            print(self.angulo)

    def draw(self, screen):
        rotated_surface = pygame.transform.rotate(self.surface_roleta, self.angulo)
        rotated_rect = rotated_surface.get_rect(center=self.pos)
        screen.blit(rotated_surface, rotated_rect.topleft)
