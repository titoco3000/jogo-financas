import pygame
from classes.roleta import Roleta
from classes.gameobject import GameObject


def run(screen, efeitos):
    GameObject.clear_scene()

    Roleta((750, 400), 250)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return {"sair": True}

        GameObject.update_all(events)
        screen.fill((0, 0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
    return {}
