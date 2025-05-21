from .gameobject import GameObject
import src.globals as globals
from .projetil import Projetil
from . import efeitos
import pygame
import math
from pygame import Vector2
from datetime import datetime, timedelta
from src.utils import sound

player_radius = 20  # tamanho do player (circulo)
player_speed = 5

tempo_delay = timedelta(seconds=0.4)


class Jogador(GameObject):
    def __init__(self, health):
        super().__init__("jogador")
        self.pos = Vector2(400, 300)

        self.teclas_pressionadas = set()

        self.buffered_inputs = []
        self.dimension = Vector2(38, 89)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - (self.pos[0] + self.dimension.x // 2)
                dy = mouse_y - (self.pos[1] + self.dimension.y // 2)
                angle = math.atan2(dy, dx)

                if globals.efeitos_no_jogador.has(efeitos.LimitarDirecoesTiro):
                    angle = round(angle / (math.pi / 2)) * (math.pi / 2)

                Projetil(
                    self.pos[0] + self.dimension.x // 2,
                    self.pos[1] + self.dimension.y // 2,
                    angle,
                )

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
        player_rect = pygame.Rect(
            self.pos.x, self.pos.y, self.dimension.x, self.dimension.y
        )
        for enemy in inimigos:
            enemy_rect = pygame.Rect(
                enemy.pos.x, enemy.pos.y, enemy.dimension.x, enemy.dimension.y
            )

            if player_rect.colliderect(enemy_rect):
                enemy.__del__()
                if globals.vida > 0:
                    globals.vida -= 1
                    sound.hit.play()

                if globals.vida <= 0:
                    sound.morte.play()
                    print("Jogador morreu")
                break

    def draw(self, screen):
        screen.blit(
            pygame.image.load("assets/sprites/char.png"), (self.pos[0], self.pos[1])
        )

        for i in range(globals.vida):
            screen.blit(
                pygame.image.load("assets/sprites/heart.png"),
                (self.pos[0] - 10, self.pos[1] + i * 10),
            )
