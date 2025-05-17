from .gameobject import GameObject
import src.globals
import pygame


class ColoredBlocker(GameObject):
    def __init__(self, color):
        super().__init__("ColoredBlocker")
        self.surface = pygame.Surface(src.globals.screen_size, pygame.SRCALPHA)
        self.surface.fill(color)

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
