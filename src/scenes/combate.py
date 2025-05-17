import pygame
from src.classes.jogador import Jogador
from src.classes.inimigo import Spawner
from src.classes.gameobject import GameObject
import src.globals as globals


def run(screen, nivel):
    GameObject.clear_scene()

    globals.inimigos_mortos_nesta_rodada = 0

    jogador = Jogador(globals.vida)
    Spawner(jogador)

    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = my_font.render(
        "Combate - pressione enter para ganhar", False, (255, 0, 0)
    )
    clock = pygame.time.Clock()

    running = True
    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                globals.sair = True
                print(globals.sair)
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        GameObject.update_all(events)

        screen.fill((0, 0, 0))
        screen.blit(text_surface, (0, 0))

        GameObject.draw_all(screen)

        pygame.display.flip()
        clock.tick(60)

        if jogador.health <= 0:
            globals.vida = 0
            running = False

        if globals.inimigos_mortos_nesta_rodada >= 5:
            running = False
