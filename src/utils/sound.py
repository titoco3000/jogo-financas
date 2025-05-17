import pygame

pygame.mixer.init()


def load(filename: str, volume: float = 1.0):
    som = pygame.mixer.Sound(filename)
    som.set_volume(volume)
    return som


fundo = load("assets/sons/fundo.wav", 0.4)
hit = load("assets/sons/colisao-projetil.wav", 1.0)
morte = load("assets/sons/morte.wav", 0.3)
morte_inimigo = load("assets/sons/morte-inimigo.wav", 1.0)
roleta = load("assets/sons/roleta.wav", 0.5)
