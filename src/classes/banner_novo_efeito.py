from .gameobject import GameObject
from .botao import Botao
from .text import Text
import pygame
import random
from src.classes.colored_blocker import ColoredBlocker

FRASES_NOVO_EFEITO = ["Aceitar", "Fazer oq", "Ah...", "...obrigado?", "OK", "...ok?"]


class BannerNovoEfeito(GameObject):
    def __init__(self, efeito, callback):
        super().__init__("BannerNovoEfeito")

        ColoredBlocker((0, 0, 0, 200))
        Botao(
            pygame.Rect(400, 500, 200, 30),
            random.choice(FRASES_NOVO_EFEITO),
            radius=10,
            on_click=callback,
        )

        Text(
            pygame.Rect(400, 200, 200, 30),
            efeito.name if efeito else "nada",
            font=pygame.font.SysFont(None, 54),
        )

        Text(
            pygame.Rect(400, 300, 200, 30),
            efeito.descrip if efeito else "Que pena... Você não ganhou nada.",
            font=pygame.font.SysFont(None, 24),
        )
