import pygame
from classes.jogador import Jogador
from classes.inimigo import Spawner
from classes.gameobject import GameObject, globals


def run(screen, nivel):
    GameObject.clear_scene()
    jogador = Jogador(globals.var.vida)
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
                globals.var.sair = True
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
            globals.var.vida = 0
            running = False
