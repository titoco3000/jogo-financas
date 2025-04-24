"""
Classe base para todos os elementos mostrados na tela.
Quando iniciado um objeto de uma classe que herde de GameObject, ele automaticamente vai ser colocada na
lista de objetos da cena. Quando removido (usando del ou chamando diretamente __del__), é retirado da lista.
A cada frame, precisam ser chamadas em algum ponto as funções update_all e draw_all.
"""

import os
import sys

# faz isso para poder importar script em nível acima
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import globals

gameobjects = []


class GameObject:
    def __init__(self, name: str):
        self.name = name
        self.globals = globals
        gameobjects.append(self)
        print("instantiate " + name)

    def __del__(self):
        try:
            gameobjects.remove(self)
        except:
            pass

    def draw(self, screen):
        pass

    def update(self, events):
        pass

    def update_all(events):
        for g in gameobjects:
            g.update(events)

    def draw_all(screen):
        for g in gameobjects:
            g.draw(screen)

    # retorna uma lista de todos os GameObjects com o nome
    def find(name):
        return [g for g in gameobjects if g.name == name]
