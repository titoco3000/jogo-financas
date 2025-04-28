import pygame
from classes.botao import Botao
from classes.gameobject import GameObject


def run(screen):
    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = my_font.render(
        "Título do jogo - pressione enter para começar", False, (255, 0, 0)
    )

    GameObject.clear_scene()
    Botao(
        pygame.rect.Rect(100, 100, 100, 100),
        "botao\n100\n200",
        border_color=(0, 0, 255),
        border_width=2,
        radius=10,
    )
    Botao(
        pygame.rect.Rect(150, 100, 100, 100),
        "botao\n100\n200",
        border_color=(0, 0, 255),
        border_width=2,
        radius=10,
    )

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return {"sair": True}

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        GameObject.update_all(events)

        screen.fill((0, 0, 0))
        screen.blit(text_surface, (0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
    return {
        "volume": 1,
        # outras configs
    }
