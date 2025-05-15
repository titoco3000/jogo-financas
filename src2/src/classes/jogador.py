from .gameobject import GameObject
from .projetil import Projetil
import pygame
import math
from pygame import Vector2

player_radius = 20  # tamanho do player (circulo)
player_speed = 5


class Jogador(GameObject):
    def __init__(self, health):
        super().__init__("jogador")
        self.pos = Vector2(400, 300)
        self.health = health
        self.morreu = False
        self.na_roleta = False  # controle para saber se está na roleta

        # Música de fundo normal
        pygame.mixer.music.load("sons/fundo.wav")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)  # Loop infinito

        # Som de hit e morte
        self.som_hit = pygame.mixer.Sound("sons/colisao-projetil.wav")
        self.som_morte = pygame.mixer.Sound("sons/morte.wav")
        self.som_hit.set_volume(1.0)
        self.som_morte.set_volume(1.0)

    def trocar_para_musica_roleta(self):
        """Troca a música de fundo para a música da roleta."""
        if not self.na_roleta and not self.morreu:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sons/roleta.wav")  # Música da roleta
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            self.na_roleta = True  # impede trocas repetidas

    def update(self, events):
        if self.morreu:
            return  # Não atualiza mais se estiver morto

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - self.pos[0]
                dy = mouse_y - self.pos[1]
                angle = math.atan2(dy, dx)
                Projetil(self.pos[0], self.pos[1], angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos[1] -= player_speed
        if keys[pygame.K_s]:
            self.pos[1] += player_speed
        if keys[pygame.K_a]:
            self.pos[0] -= player_speed
        if keys[pygame.K_d]:
            self.pos[0] += player_speed

        inimigos = GameObject.find("inimigo")
        for enemy in inimigos:
            distancia = math.hypot(self.pos.x - enemy.pos.x, self.pos.y - enemy.pos.y)
            if distancia < enemy.radius + player_radius:
                enemy.__del__()

                if self.health > 0:
                    self.health -= 1
                    self.som_hit.play()

                if self.health <= 0 and not self.morreu:
                    self.morreu = True
                    print("Jogador morreu")
                    self.som_morte.play()
                    pygame.mixer.music.stop()  # Para a música ao morrer

                break

    def draw(self, screen):
        if not self.morreu:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), player_radius)


