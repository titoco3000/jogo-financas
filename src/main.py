import pygame

pygame.init()
pygame.font.init()

from src.scenes import menu_inicial, combate, menu_entre_niveis, menu_fim
import src.globals as globals

screen = pygame.display.set_mode(globals.screen_size)

import src.classes.efeitos as efeitos

# Adiciona efeito como teste
# globals.efeitos_no_jogador.add(efeitos.LimitarDirecoesTiro)
# globals.efeitos_no_jogador.add(efeitos.ZigZagProjetil)
# globals.efeitos_no_jogador.add(efeitos.DelayMovimentacao)

while not globals.sair:
    # inicio de uma run
    menu_inicial.run(screen)

    if globals.sair:
        break

    for nivel in range(1000):
        combate.run(screen, nivel)

        if globals.sair:
            break

        if globals.vida <= 0:
            menu_fim.run(screen)
            if globals.sair:
                break
        else:
            menu_entre_niveis.run(screen)
            if globals.sair:
                break

    pygame.quit()
