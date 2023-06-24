import pygame
from constantes import *

# Obtener una superficie desde un sprite
def getSuperfaceFromSpriteSheet():
    lista = []
    return lista


class Player:

    def __init__(self) -> None:
        
        self.walk = [] # En la medida que vaya caminando va a ir pasando de una superficie a la otra

        self.stay = [] # Mientras el personaje se encuentra quieto

        self.frame = 0 # Cada fotograma que compone la imagen, para animar al personaje

        


