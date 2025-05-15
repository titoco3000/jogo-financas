import pygame
from classes.roleta import Roleta
from classes.gameobject import GameObject, globals


def run(screen):
    GameObject.clear_scene()

    Roleta((750, 400), 250)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                globals.var.sair = True
                return

        GameObject.update_all(events)
        screen.fill((0, 0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
