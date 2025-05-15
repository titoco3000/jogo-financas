class Efeito:
    def __init__(self, name: str, descrip: str):
        self.name = name
        self.descrip = descrip


class Efeitos:
    def __init__(self):
        self.atuais = []

    def add(self, efeito: Efeito):
        self.atuais.append(efeito())

    def has(self, tipo):
        return any(isinstance(x, tipo) for x in self.atuais)


class DelayInput(Efeito):
    def __init__(self):
        super().__init__("Estagnação econômica", "Causa um delay no input")


# não implementado
class Publicidade(Efeito):
    def __init__(self):
        super().__init__(
            "Publicidade excessiva", "Interrompe o jogo com banners publicitários"
        )


class LimitarDirecoesTiro(Efeito):
    def __init__(self):
        super().__init__("Monopólio", "Limita as direções que você pode atirar")


class ZigZagProjetil(Efeito):
    def __init__(self):
        super().__init__("Mercado instável", "Os tiros seguem em zigue-zague")
