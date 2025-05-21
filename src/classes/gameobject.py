"""
Classe base para todos os elementos mostrados na tela.
Quando iniciado um objeto de uma classe que herde de GameObject, ele automaticamente vai ser colocada na
lista de objetos da cena. Quando removido (usando del ou chamando diretamente __del__), é retirado da lista.
A cada frame, precisam ser chamadas em algum ponto as funções update_all e draw_all.
"""

gameobjects = []


class GameObject:
    def __init__(self, name: str, render_priority: int = 0):
        self.name = name
        self.render_priority = render_priority
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
        # Cria uma cópia da lista e a ordena com base na render_priority
        # Objetos com prioridade maior serão desenhados depois (por cima)
        sorted_gameobjects = sorted(gameobjects, key=lambda g: g.render_priority)
        for g in sorted_gameobjects:
            g.draw(screen)

    # retorna uma lista de todos os GameObjects com o nome
    def find(name):
        return [g for g in gameobjects if g.name == name]

    def clear_scene():
        global gameobjects
        gameobjects = []
