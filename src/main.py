import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption("Jogo das BETs")

from src.scenes import menu_inicial, menu_intro, combate, menu_entre_niveis, menu_fim
import src.globals as globals

screen = pygame.display.set_mode(globals.screen_size)

import src.classes.efeitos as efeitos

# Adiciona efeito como teste
# globals.efeitos_no_jogador.add(efeitos.Publicidade)
# globals.efeitos_no_jogador.add(efeitos.ZigZagProjetil)
# globals.efeitos_no_jogador.add(efeitos.DelayMovimentacao)

from src.utils import sound

sound.fundo.play(-1)

while not globals.sair:
    # inicio de uma run
    menu_inicial.run(screen)

    if globals.sair:
        break

    menu_intro.run(screen)

    if globals.sair:
        break

    for nivel in range(1000):
        combate.run(screen, nivel)

        if globals.sair:
            break

        if globals.vida <= 0:
            menu_fim.run(screen)
            break
        if globals.roleta:
            globals.roleta = False
            print(globals.roleta)
            menu_entre_niveis.run(screen)
            if globals.sair:
                break

pygame.quit()
