"""
Arquivo que guarda todas as variaveis, constantes ou não, que devem ser acessíveis globalmente.
"""

from pygame import Vector2
from src.classes.efeitos import Efeitos

screen_size = Vector2(960, 720)

efeitos_no_jogador = Efeitos()
sair = False
roleta = False
jogadas = 0
volume = 1
vida = 2
max_ammo = 5
inimigos_mortos_nesta_rodada = 0
mortestotais = 0


def reset():
    global efeitos_no_jogador, sair, roleta, jogadas, volume, vida, max_ammo, inimigos_mortos_nesta_rodada, mortestotais
    efeitos_no_jogador.atuais = []
    sair = False
    roleta = False
    jogadas = 0
    vida = 2
    max_ammo = 5
    inimigos_mortos_nesta_rodada = 0
    mortestotais = 0