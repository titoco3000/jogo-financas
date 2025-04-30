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
    (0, 0.3),
    (-10, 0.2),
    (-12, 0.3),
    (-10, 0.3),
    (3 * 360, 1),
    (3 * 360 + 10, 0.1),
    (3 * 360 + 12, 0.2),
    (3 * 360, 0.3),
]


class Roleta(GameObject):
    def __init__(self, pos, radius):
        super().__init__("roleta")
        self.surface_roleta = pygame.Surface(
            (2 * radius, 2 * radius), pygame.SRCALPHA, 32
        )

        fatias = 10
        seccoes = [
            (pygame.color.THECOLORS["red"], "1111"),
            (pygame.color.THECOLORS["blue"], "2222"),
            (pygame.color.THECOLORS["green"], "3333"),
            (pygame.color.THECOLORS["yellow"], "4444"),
            (pygame.color.THECOLORS["pink"], "5555"),
            (pygame.color.THECOLORS["red"], "6666"),
            (pygame.color.THECOLORS["blue"], "7777"),
            (pygame.color.THECOLORS["green"], "8888"),
            (pygame.color.THECOLORS["yellow"], "9999"),
            (pygame.color.THECOLORS["pink"], "1010"),
        ]

        fontsize = int(0.1 * radius)
        self.font = pygame.font.SysFont(None, fontsize)

        largura_fatia = int(360 / fatias)
        for fatia in range(fatias):
            pie_piece(
                self.surface_roleta,
                Vector2(radius, radius),
                radius,
                seccoes[fatia][0],
                fatia * largura_fatia,
                math.ceil((fatia + 1) * largura_fatia) + 1,
            )

        for fatia in range(fatias):
            angle_deg = fatia * largura_fatia
            angle_rad = math.radians(angle_deg)

            text_surface = self.font.render(seccoes[fatia][1], True, (255, 255, 255))
            rotated_text = pygame.transform.rotate(text_surface, -angle_deg)

            text_radius = radius * 0.8

            text_x = radius + text_radius * math.sin(angle_rad)
            text_y = radius - text_radius * math.cos(angle_rad)
            text_rect = rotated_text.get_rect(center=(text_x, text_y))
            self.surface_roleta.blit(rotated_text, text_rect)

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
            # print(self.angulo)

    def draw(self, screen):
        rotated_surface = pygame.transform.rotate(self.surface_roleta, self.angulo)
        rotated_rect = rotated_surface.get_rect(center=self.pos)
        screen.blit(rotated_surface, rotated_rect.topleft)
