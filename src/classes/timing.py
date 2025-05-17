from .gameobject import GameObject
import time


class Timer(GameObject):
    """
    Invoca uma função depois de um intervalo
    """

    def __init__(self, func, delay):
        super().__init__("timer")
        self.func = func
        self.delay = delay
        self.start = time.time()

    def update(self, _):
        if time.time() - self.start > self.delay:
            self.func()
            self.__del__()
