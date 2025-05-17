import random


class Efeito:
    name = ""
    descrip = ""


class Efeitos:
    def __init__(self):
        self.atuais = []

    def add(self, efeito: Efeito):
        self.atuais.append(efeito())

    def has(self, tipo):
        return any(isinstance(x, tipo) for x in self.atuais)

    def escolher_novo_efeito(self):
        opcoes = [DelayMovimentacao, Publicidade, LimitarDirecoesTiro, ZigZagProjetil]
        random.shuffle(opcoes)
        for item in opcoes:
            if not self.has(item):
                return item
        return None


class DelayMovimentacao(Efeito):
    name = "Estagnação econômica"
    descrip = "Causa um delay no input de movimentação"


# não implementado
class Publicidade(Efeito):
    name = "Publicidade excessiva"
    descrip = "Interrompe o jogo com banners publicitários"


class LimitarDirecoesTiro(Efeito):
    name = "Monopólio"
    descrip = "Limita as direções que você pode atirar"


class ZigZagProjetil(Efeito):
    name = "Mercado instável"
    descrip = "Os tiros saem em zigue-zague"
