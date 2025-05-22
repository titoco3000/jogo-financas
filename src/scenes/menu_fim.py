import pygame
from src.classes.botao import Botao
from src.classes.text import Text
from src.classes.gameobject import GameObject
import src.globals as globals


def run(screen):
    running = True

    def voltar_menu():
        nonlocal running
        running = False
        globals.reset()

    background = pygame.image.load("assets/sprites/menuinv.png")
    if globals.jogadas == 0:
        text = Text((100,100), "final1")
    elif globals.jogadas < 5:
        text = Text((100,100), "final2")
    else:
        text = Text((100,100), "final3")

    GameObject.clear_scene()
    Botao(
        pygame.rect.Rect(340, 500, 300, 50),
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
        screen.blit(background, (0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
