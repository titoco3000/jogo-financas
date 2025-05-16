"""
Arquivo que guarda todas as variaveis, constantes ou não, que devem ser acessíveis globalmente.
"""

from pygame import Vector2
from src.classes.efeitos import Efeitos

screen_size = Vector2(1000, 700)

efeitos_no_jogador = Efeitos()
sair = False
volume = 1
vida = 2
