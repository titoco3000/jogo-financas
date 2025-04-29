import time

import globals.utils
from .gameobject import globals


class Animation:
    """
    Faz uma interpolação linear entre pontos de uma animação.

    keyframes é uma lista de (valor, tempo), onde valor é um
    vetor ou escalar e tempo, o intervalo desde o keyframe anterior.

    Todos os valores devem ter a mesma dimensão.
    get_state retorna um vetor dessa dimensão com base nos pontos
    """

    def __init__(self, keyframes):
        self.keyframes = keyframes
        self.start_time = time.time()

        # Construir linha do tempo cumulativa
        self.timeline = []
        t = 0
        for value, dt in keyframes:
            self.timeline.append((value, t))
            t += dt
        self.total_duration = t  # duração total da animação
        self.playing = False

    def reset(self):
        self.start_time = time.time()
        self.playing = False

    def play(self):
        self.playing = True

    def get_state(self):
        current_time = time.time() - self.start_time

        # Se o tempo for antes do primeiro keyframe
        if current_time <= self.timeline[0][1]:
            return self.timeline[0][0]

        # Se o tempo for depois do último keyframe
        if current_time >= self.timeline[-1][1]:
            self.playing = False
            return self.timeline[-1][0]

        # Procurar o intervalo certo
        for i in range(len(self.timeline) - 1):
            a_val, a_time = self.timeline[i]
            b_val, b_time = self.timeline[i + 1]

            if a_time <= current_time <= b_time:
                t = (current_time - a_time) / (b_time - a_time)
                return globals.utils.lerp(a_val, b_val, t)

        # Se não encontrar (não deveria acontecer)
        raise Exception("Tempo fora dos keyframes.")
