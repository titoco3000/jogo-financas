from .gameobject import GameObject
import src.globals as globals
from .projetil import Projetil
from . import efeitos
import pygame
import math
from pygame import Vector2
from datetime import datetime, timedelta

player_radius = 20  # tamanho do player (circulo)
player_speed = 5

tempo_delay = timedelta(seconds=0.4)


class Jogador(GameObject):
    def __init__(self, health):
        super().__init__("jogador")
        self.pos = Vector2(400, 300)
        self.health = health
        self.teclas_pressionadas = set()

        self.buffered_inputs = []

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.dx = mouse_x - self.pos[0]
                self.dy = mouse_y - self.pos[1]
                angle = math.atan2(self.dy, self.dx)

                if globals.efeitos_no_jogador.has(efeitos.LimitarDirecoesTiro):
                    angle = round(angle / (math.pi / 2)) * (math.pi / 2)

                Projetil(self.pos[0], self.pos[1], angle)

            elif event.type == pygame.KEYDOWN:
                self.teclas_pressionadas.add(event.key)
            elif event.type == pygame.KEYUP:
                self.teclas_pressionadas.discard(event.key)

        direction_input = Vector2(0, 0)

        # movimentação baseada nas teclas pressionadas
        if pygame.K_a in self.teclas_pressionadas:
            direction_input.x -= 1
        if pygame.K_d in self.teclas_pressionadas:
            direction_input.x += 1
        if pygame.K_w in self.teclas_pressionadas:
            direction_input.y -= 1
        if pygame.K_s in self.teclas_pressionadas:
            direction_input.y += 1

        usar_delay = globals.efeitos_no_jogador.has(efeitos.DelayMovimentacao)

        now = datetime.now()

        if usar_delay:
            print(len(self.buffered_inputs))
            # Only buffer new movement if there is some input
            if direction_input.magnitude() > 0:
                direction_input = direction_input.normalize()
                self.buffered_inputs.append((now, direction_input))

            # Only move if the oldest buffered input has expired
            if self.buffered_inputs and now - self.buffered_inputs[0][0] >= tempo_delay:
                _, move_dir = self.buffered_inputs.pop(0)
                self.pos += move_dir * player_speed
        else:
            if direction_input.magnitude() > 0:
                direction_input = direction_input.normalize()
                self.pos += direction_input * player_speed

        inimigos = GameObject.find("inimigo")
        for enemy in inimigos:
            if (
                math.sqrt(
                    (self.pos.x - enemy.pos.x) ** 2 + (self.pos.y - enemy.pos.y) ** 2
                )
                < enemy.radius + player_radius
            ):
                enemy.__del__()
                if self.health > 0:
                    self.health -= 1
                if self.health <= 0:
                    print("Jogador morreu")
                break

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), player_radius
        )
