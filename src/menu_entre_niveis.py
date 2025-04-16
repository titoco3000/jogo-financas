import pygame
from pygame import Vector2
import math

def pie_piece(surface, pos:Vector2, raio, cor, inicio, fim):
    p = [pos]
    for n in range(inicio,fim):
        x = pos.x + int(raio*math.cos(n*math.pi/180))
        y = pos.y + int(raio*math.sin(n*math.pi/180))
        p.append(Vector2(x, y))
    p.append(pos)
    
    if len(p) > 2:
        pygame.draw.polygon(surface, cor, p)


def run(screen, efeitos):
    roleta = pygame.Surface((500, 500))

    fatias = 10
    largura_fatia = int(360/fatias)
    for fatia in range(fatias):    
        pie_piece(roleta, Vector2(250,250),250,(255,0,0),fatia*largura_fatia,(fatia+1)*largura_fatia)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {"sair":True}
            
        screen.fill((0,0,0))
        screen.blit(roleta, (250,250))

        pygame.display.flip()
    return {}

