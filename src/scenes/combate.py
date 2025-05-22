import pygame
from src.classes.botao import Botao
from src.classes.jogador import Jogador
from src.classes.inimigo import Spawner
from src.classes.gameobject import GameObject
import src.globals as globals
from src.classes.publicidade import Publicidade
import src.classes.efeitos as efeitos


def run(screen, nivel):
    def rodarroleta():
        nonlocal running
        if globals.roleta == False:
            globals.roleta = True
            globals.jogadas += 1
            if globals.jogadas == 1:
                globals.max_ammo -= 1
            if globals.jogadas == 5:
                globals.max_ammo -= 3
        running = False

    GameObject.clear_scene()

    globals.inimigos_mortos_nesta_rodada = 0

    jogador = Jogador()
    Spawner(jogador)

    if globals.efeitos_no_jogador.has(efeitos.Publicidade):
        Publicidade()

    if globals.jogadas == 0:
        background = pygame.image.load("assets/sprites/background1.png")
    elif globals.jogadas < 5:
        background = pygame.image.load("assets/sprites/background2.png")
    else:
        background = pygame.image.load("assets/sprites/background3.png")

    clock = pygame.time.Clock()

    running = True
    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                globals.sair = True
                print(globals.sair)
                return

        GameObject.update_all(events)

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        GameObject.draw_all(screen)

        pygame.display.flip()
        clock.tick(60)

        if globals.vida <= 0:
            running = False

        if globals.inimigos_mortos_nesta_rodada >= 10 and globals.jogadas < 5:
            Botao(
                pygame.rect.Rect(75, 590, 120, 50),
                "Rodar roleta",
                border_color=(100, 100, 100),
                border_width=2,
                radius=10,
                on_click=rodarroleta,
            )
