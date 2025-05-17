from .gameobject import GameObject
import src.globals as globals
from .animation import Animation
import pygame
from pygame import Vector2
import math
from src.utils import sound


def create_surface_roleta(fatias, radius, font):

    def pie_piece(surface, pos: Vector2, raio, cor, inicio, fim):
        p = [pos]
        for n in range(inicio, fim):
            x = pos.x + int(raio * math.cos(n * math.pi / 180))
            y = pos.y + int(raio * math.sin(n * math.pi / 180))
            p.append(Vector2(x, y))
        p.append(pos)

        if len(p) > 2:
            pygame.draw.polygon(surface, cor, p)

    surface_roleta = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)

    largura_fatia = int(360 / len(fatias))
    for fatia in range(len(fatias)):
        pie_piece(
            surface_roleta,
            Vector2(radius, radius),
            radius,
            fatias[fatia][0],
            fatia * largura_fatia,
            math.ceil((fatia + 1) * largura_fatia) + 1,
        )

    for fatia in range(len(fatias)):
        angle_deg = (fatia + 3) * largura_fatia
        angle_rad = math.radians(angle_deg)

        text_surface = font.render(fatias[fatia][1], True, (255, 255, 255))
        rotated_text = pygame.transform.rotate(text_surface, -angle_deg)

        text_radius = radius * 0.8

        text_x = radius + text_radius * math.sin(angle_rad)
        text_y = radius - text_radius * math.cos(angle_rad)
        text_rect = rotated_text.get_rect(center=(text_x, text_y))
        surface_roleta.blit(rotated_text, text_rect)

    return surface_roleta


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
    def __init__(self, pos, radius, labels):
        super().__init__("roleta")

        self.fatias = [
            (pygame.color.THECOLORS["red"], labels[0]),
            (pygame.color.THECOLORS["blue"], labels[1]),
            (pygame.color.THECOLORS["green"], labels[2]),
            ((206, 155, 16), labels[3]),
            ((226, 32, 229), labels[4]),
            (pygame.color.THECOLORS["red"], labels[5]),
            (pygame.color.THECOLORS["blue"], labels[6]),
            (pygame.color.THECOLORS["green"], labels[7]),
            ((206, 155, 16), labels[8]),
            ((226, 32, 229), labels[9]),
        ]

        fontsize = int(0.1 * radius)
        self.font = pygame.font.SysFont(None, fontsize)

        self.pos = pos
        self.radius = radius
        self.angulo = 0

        self.surface_roleta = create_surface_roleta(self.fatias, self.radius, self.font)

        self.anim = Animation(ANIMACAO_GIRO)
        self.ponto_critico = False
        self.rodar()

    def rodar(self):
        sound.roleta.play()

        self.anim.reset()
        self.anim.play()

    def set_winner(self, label):
        self.fatias[7] = (self.fatias[7][0], label)
        self.surface_roleta = create_surface_roleta(self.fatias, self.radius, self.font)

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # self.rodar()
                    pass

        if self.anim.playing:
            self.angulo = self.anim.get_state()
            if self.angulo > 270 and not self.ponto_critico:
                self.ponto_critico = True

    def draw(self, screen):
        rotated_surface = pygame.transform.rotate(self.surface_roleta, self.angulo)
        rotated_rect = rotated_surface.get_rect(center=self.pos)
        screen.blit(rotated_surface, rotated_rect.topleft)
