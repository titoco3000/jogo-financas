import pygame
from src.classes.botao import Botao
from src.classes.gameobject import GameObject
import src.globals as globals


def run(screen):
    running = True
    
    def iniciar_jogo():
        nonlocal running
        running = False

    background = pygame.image.load("assets/sprites/menu.png")
    title = pygame.image.load("assets/sprites/title.png")

    GameObject.clear_scene()
    Botao(
        pygame.rect.Rect(330, 500, 300, 50),
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
        screen.blit(background, (0, 0))
        screen.blit(title, (182, 50))
        GameObject.draw_all(screen)

        pygame.display.flip()

    globals.volume = 1
    # outras configs

    return
