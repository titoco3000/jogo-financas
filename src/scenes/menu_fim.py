import pygame
from src.classes.botao import Botao
from src.classes.gameobject import GameObject
import src.globals as globals


def run(screen):
    running = True

    def voltar_menu():
        nonlocal running
        running = False
        globals.reset()

    GameObject.clear_scene()
    Botao(
        pygame.rect.Rect(100, 200, 200, 50),
        "Voltar ao menu",
        border_color=(100, 100, 100),
        border_width=2,
        radius=10,
        on_click=voltar_menu,
    )

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                globals.sair = True
                return

        GameObject.update_all(events)

        screen.fill((0, 0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
