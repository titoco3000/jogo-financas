import pygame
from pygame import Vector2
import menu_inicial
import combate
import menu_entre_niveis
import menu_fim


def main():
    pygame.init()

    screen_size = Vector2(1000, 700)

    screen = pygame.display.set_mode(screen_size)
    pygame.font.init() 


    running = True
    while running:
        # inicio de uma run
        configs = menu_inicial.run(screen)
        efeitos = {}

        if configs.get("sair"):
            running = False

        status = {
            "vida":10,
            "dinheiro":10
        }

        for nivel in range(1000):
            status = combate.run(screen, efeitos, nivel, status)
            if status.get("sair"):
                running = False
                break

            if status.get("vida") <= 0:
                menu_fim.run(screen)
                break

            efeitos = menu_entre_niveis.run(screen, efeitos)
            if efeitos.get("sair"):
                running = False
                break
        
        pygame.quit()


if __name__ == "__main__":
    main()