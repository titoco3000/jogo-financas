import globals.var
import pygame
from classes.gameobject import globals


def run(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.var.sair = True
                return

        screen.fill((0, 0, 0))

        pygame.display.flip()
