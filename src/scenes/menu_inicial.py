import pygame
from classes.botao import Botao
from classes.gameobject import GameObject


def run(screen):
    running = True

    def iniciar_jogo():
        nonlocal running
        print("a")
        running = False

    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = my_font.render(
        "Título do jogo - precisamos desenhar esse menu", False, (255, 255, 255)
    )

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
                return {"sair": True}

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        GameObject.update_all(events)

        screen.fill((0, 0, 0))
        screen.blit(text_surface, (100, 100))
        GameObject.draw_all(screen)

        pygame.display.flip()
    return {
        "volume": 1,
        # outras configs
    }
