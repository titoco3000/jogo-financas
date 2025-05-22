from .gameobject import GameObject
import src.globals as globals
from .projetil import Projetil
from . import efeitos
import pygame
import math
from pygame import Vector2
from datetime import datetime, timedelta
from src.utils import sound
from src.classes.timing import Repeater

player_radius = 20  # tamanho do player (circulo)
player_speed = 5

tempo_delay = timedelta(seconds=0.3)
intervalo_entre_tiros = timedelta(seconds=0.15)


class Jogador(GameObject):
    def __init__(self):
        super().__init__("jogador")
        self.pos = Vector2(400, 300)

        self.teclas_pressionadas = set()

        self.buffered_inputs = []
        self.dimension = Vector2(38, 89)
        self.ammo = 2

        # self.display_bullet = Projetil(-10, -10, 0, False)

        self.font = pygame.font.SysFont(None, 24)
        self.ultimo_tiro = datetime.now()

        def ammo_up():
            self.ammo = min(globals.max_ammo, self.ammo + 1)

        # Aumenta a quantidade de balas a intervalos
        Repeater(ammo_up, 1)

    def update(self, events):
        now = datetime.now()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.ammo > 0 and now - self.ultimo_tiro >= intervalo_entre_tiros:
                    self.ultimo_tiro = now
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
                    self.ammo -= 1

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

        if usar_delay:
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

        # self.display_bullet.x = self.pos.x + self.dimension.x
        # self.display_bullet.y = self.pos.y - 10

    def draw(self, screen):
        if globals.jogadas == 0:
            screen.blit(pygame.image.load("assets/sprites/char1.png"), (self.pos[0], self.pos[1]))
        elif globals.jogadas < 5:
            screen.blit(pygame.image.load("assets/sprites/char2.png"), (self.pos[0], self.pos[1]))
        else:
            screen.blit(pygame.image.load("assets/sprites/char3.png"), (self.pos[0], self.pos[1]))

        for i in range(globals.vida):
            screen.blit(
                pygame.image.load("assets/sprites/heart.png"),
                (self.pos[0] - 10, self.pos[1] + i * 10),
            )

        ammo_count = self.font.render("$" * self.ammo, True, (255, 255, 255))
        screen.blit(ammo_count, (self.pos.x + self.dimension.x, self.pos.y - 10))
