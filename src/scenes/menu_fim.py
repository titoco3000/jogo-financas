import pygame
import src.globals as globals


def run(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.sair = True
                return

        screen.fill((0, 0, 0))

        pygame.display.flip()
