import pygame
from src.classes.gameobject import GameObject
from src.classes.roleta import Roleta
from src.classes.timing import Timer
from src.classes.banner_novo_efeito import BannerNovoEfeito
import src.globals as globals
import time
import random

PROMESSAS_VAZIAS = [
    "+vida",
    "$$$",
    "+velocidade",
    "prêmios!",
    "ajudante",
    "rodada bônus",
    "-inimigos",
    "inimigos lentos",
    "+tiros",
    "regeneração",
    "efeito fantasma",
]


def run(screen):
    running = True

    def iniciar_proximo_combate():
        nonlocal running
        running = False

    GameObject.clear_scene()

    random.shuffle(PROMESSAS_VAZIAS)

    roleta = Roleta((750, 400), 250, PROMESSAS_VAZIAS)

    trocou_label = False
    rodou = False

    roleta.rodar()

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                globals.var.sair = True
                return

        GameObject.update_all(events)

        if not trocou_label and roleta.ponto_critico:
            trocou_label = True
            novo_efeito = globals.var.efeitos_no_jogador.escolher_novo_efeito()
            if novo_efeito:
                globals.var.efeitos_no_jogador.add(novo_efeito)
                roleta.set_winner(novo_efeito().name)
            else:
                roleta.set_winner("nada")

        if not rodou and roleta.anim.done:
            rodou = True

            # Inicia Gameobject depois de um delay
            Timer(lambda: BannerNovoEfeito(novo_efeito, iniciar_proximo_combate), 2)

        screen.fill((0, 0, 0))
        GameObject.draw_all(screen)

        pygame.display.flip()
