import pygame
import globals
from scenes import menu_inicial, combate, menu_entre_niveis, menu_fim
import globals


def main():
    pygame.init()

    screen = pygame.display.set_mode(globals.screen_size)
    pygame.font.init()

    # status inicial
    status = {"vida": 2, "dinheiro": 10}

    while not status.get("sair", False):
        # inicio de uma run
        configs = menu_inicial.run(screen, status)

        if configs.get("sair"):
            running = False
            break

        for nivel in range(1000):
            status = combate.run(screen, nivel, status)

            if status.get("sair", False):
                break

            if status.get("vida") <= 0:
                status = menu_fim.run(screen, status)
                if status.get("sair", False):
                    break
            else:
                status = menu_entre_niveis.run(screen, status)
                if status.get("sair", False):
                    break

        pygame.quit()


if __name__ == "__main__":
    main()
