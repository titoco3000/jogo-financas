from .gameobject import GameObject
import pygame
from pygame import Vector2
import math
import random

enemy_radius = 15  # tamanho do inimigo
enemy_speed = 2  # movimento
enemy_spawn_distance = (
    300  # distancia minima para spawn de inimigos (quanto maior mais longe ele spawna)
)
enemy_spawn_cooldown = 2000  # cooldown de spawn (milissegundos)


class Spawner(GameObject):
    def __init__(self, ref_jogador):
        super().__init__("spawner_inimigos")
        self.ref_jogador = ref_jogador
        self.last_enemy_spawn_time = pygame.time.get_ticks()

    def update(self, events):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_enemy_spawn_time > enemy_spawn_cooldown:
            self.spawn_enemy()
            self.last_enemy_spawn_time = current_time

    def spawn_enemy(self):
        angle = random.uniform(0, 2 * math.pi)  # angulo aleatorio para pos do inimigo

        # distancia aleatoria de spawn que sera entre 300 (valor de enemy_spawn_distance) e 400 (somado +100)
        distance = random.randint(enemy_spawn_distance, enemy_spawn_distance + 100)

        enemy_x = self.ref_jogador.pos.x + math.cos(angle) * distance
        enemy_y = self.ref_jogador.pos.y + math.sin(angle) * distance

        Inimigo(self.ref_jogador, Vector2(enemy_x, enemy_y))


# Inimigo que segue o jogador
class Inimigo(GameObject):
    def __init__(self, ref_jogador, pos_inicial: Vector2, health=2):
        super().__init__("inimigo")
        self.ref_jogador = ref_jogador
        self.pos = pos_inicial
        self.health = health
        self.radius = enemy_radius

    def update(self, events):
        dx = self.ref_jogador.pos.x - self.pos.x
        dy = self.ref_jogador.pos.y - self.pos.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 5:
            self.pos.x += (dx / distance) * enemy_speed
            self.pos.y += (dy / distance) * enemy_speed

    def draw(self, screen):
        pygame.draw.circle(
            screen, (0, 255, 0), (int(self.pos[0]), int(self.pos[1])), enemy_radius
        )
