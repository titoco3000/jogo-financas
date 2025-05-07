import pygame
import globals.var
from scenes import menu_inicial, combate, menu_entre_niveis, menu_fim
import globals


def main():
    pygame.init()

    screen = pygame.display.set_mode(globals.var.screen_size)
    pygame.font.init()

    running = True
    while running:
        # inicio de uma run
        configs = menu_inicial.run(screen)
        efeitos = {}

        if configs.get("sair"):
            running = False
            break

        status = {"vida": 10, "dinheiro": 10}

        for nivel in range(1000):
            status = combate.run(screen, efeitos, nivel, status)
            if status.get("sair"):
                running = False
                break

            elif status.get("vida") <= 0:
                status = menu_fim.run(screen)
                if status.get("sair"):
                    running = False
                    break
            else:
                efeitos = menu_entre_niveis.run(screen, efeitos)
                if efeitos.get("sair"):
                    running = False
                    break

        pygame.quit()


if __name__ == "__main__":
    main()
