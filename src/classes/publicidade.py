from .gameobject import GameObject
import pygame
from pygame import Vector2
import random
from src.globals import screen_size
import math

frases = [
    "A vida é uma roleta, aposte no que você ama.",
    "Aposte na sua felicidade, aposte SUPERBETS.",
    "O que é melhor que não ter dinheiro? Ter. Aposte.",
    "Trabalhar é sorte. Apostar é estratégia.",
    "Seu futuro está a um clique... ou a uma dívida.",
    "Esqueça o amanhã, jogue hoje.",
    "Não tem nada a perder? Perfeito. DEPRESSOBETS.",
    "Seu salário nunca teve tanto potencial quanto na HEXABETS",
    "Diversão garantida, lucros opcionais. MEGABETS",
    "Confie no destino. Ele sempre vence.",
    "Para quê plano de carreira, se existe sorte?",
    "Invista como os ricos. Perca como nunca.",
    "O sistema quer que você perca. Prove que consegue mais (às vezes).",
    "A esperança é a última que aposta.",
    "Mais que um jogo: uma fuga da realidade.",
    "Onde o impossível é improvável — até acontecer.",
    "Não é vício, é estilo de vida.",
    "Problemas financeiros? Aposte neles.",
    "Sua chance de mudar de vida* (*estatisticamente nula)",
    "Jogando você não perde tempo. Só dinheiro.",
    "Ganhar é raro. Jogar é inevitável.",
    "Aposte agora. Lamente depois.",
    "Eles têm herança. Você tem esperança.",
    "Entre pobres e milionários, há um bilhete de distância. MONEYBETS",
    "Prometemos emoção. Nunca lucros.",
    "A estatística está contra você. E nós também.",
]

cores = [
    pygame.Color("red"),
    pygame.Color("blue"),
    pygame.Color("green"),
    pygame.Color("yellow"),
    pygame.Color("purple"),
    pygame.Color("orange"),
    pygame.Color("pink"),
]


class Publicidade(GameObject):
    def __init__(self):
        super().__init__("publicidade", render_priority=10)
        self.font = pygame.font.Font("assets/fonts/SAIBA-45.ttf", 100)
        self.speed = 0.5
        self.reset()
        self.last_tick = pygame.time.get_ticks()

    def reset(self):
        frase = random.choice(frases)
        self.angulo = random.uniform(0, 360)

        self.text_surface = self.font.render(frase, True, random.choice(cores))
        self.text_surface = pygame.transform.rotate(
            self.text_surface,
            self.angulo + (180 if self.angulo > 120 and self.angulo < 270 else 0),
        )

        self.text_rect = self.text_surface.get_rect()

        max_text_dim = max(
            self.text_surface.get_width(), self.text_surface.get_height()
        )
        buffer = max_text_dim * 1.01

        expanded_width = screen_size.x + buffer * 1
        expanded_height = screen_size.y + buffer * 1

        max_travel_distance = math.sqrt(expanded_width**2 + expanded_height**2) / 2

        screen_center = pygame.math.Vector2(screen_size.x // 2, screen_size.y // 2)

        self.start = pygame.math.Vector2()
        self.end = pygame.math.Vector2()

        self.start.from_polar((max_travel_distance, -self.angulo + 180))
        self.end.from_polar((max_travel_distance, -self.angulo))

        self.start += screen_center
        self.end += screen_center

        travel_distance = self.start.distance_to(self.end)

        self.duration = travel_distance / self.speed

        self.current_pos = self.start.copy()
        self.time_elapsed = 0

    def update(self, events):
        delta_time = pygame.time.get_ticks() - self.last_tick
        self.last_tick = pygame.time.get_ticks()
        self.time_elapsed += delta_time

        t = min(1.0, self.time_elapsed / self.duration)

        self.current_pos = self.start.lerp(self.end, t)

        self.text_rect.center = self.current_pos

        if t >= 1.0:
            self.reset()

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect.topleft)
        # pygame.draw.rect(screen, (0, 255, 0), self.text_rect, 2)

        # pygame.draw.line(
        #     screen,
        #     (255, 0, 0),
        #     self.start,
        #     self.end,
        #     2,
        # )
