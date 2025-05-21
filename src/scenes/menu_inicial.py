import pygame
from src.classes.botao import Botao
from src.classes.gameobject import GameObject
import src.globals as globals


def run(screen):
    running = True

    def iniciar_jogo():
        nonlocal running
        print("a")
        running = False

    GameObject.clear_scene()
    Botao(
        pygame.rect.Rect(100, 200, 100, 50),
        "Iniciar jogo",
        border_color=(100, 100, 100),
        border_width=2,
        radius=10,
        on_click=iniciar_jogo,
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

    globals.volume = 1
    # outras configs

    return
