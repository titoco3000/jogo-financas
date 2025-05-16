import pygame
from src.classes.roleta import Roleta
from src.classes.gameobject import GameObject
import src.globals as globals


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
