import pygame
from src.scenes import menu_inicial, combate, menu_entre_niveis, menu_fim
import src.globals as globals
import src.classes.efeitos as efeitos


def main():
    pygame.init()

    screen = pygame.display.set_mode(globals.var.screen_size)
    pygame.font.init()

    # Adiciona efeito como teste
    # globals.var.efeitos_no_jogador.add(efeitos.LimitarDirecoesTiro)
    # globals.var.efeitos_no_jogador.add(efeitos.ZigZagProjetil)
    # globals.var.efeitos_no_jogador.add(efeitos.DelayMovimentacao)

    while not globals.var.sair:
        # inicio de uma run
        menu_inicial.run(screen)

        if globals.var.sair:
            break

        for nivel in range(1000):
            combate.run(screen, nivel)
            print("sai do combate, devo sair do jogo? ", globals.var.sair)

            if globals.var.sair:
                break

            if globals.var.vida <= 0:
                menu_fim.run(screen)
                if globals.var.sair:
                    break
            else:
                menu_entre_niveis.run(screen)
                if globals.var.sair:
                    break
        print("saí do loop de fases, devo sair do jogo? ", globals.var.sair)

        pygame.quit()


if __name__ == "__main__":
    main()
