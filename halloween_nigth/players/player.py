import pygame
from halloween_nigth.constantes import *

# Obtener una superficie desde un sprite
def getSuperfaceFromSpriteSheet(path, columnas, filas):
    lista = []

    superficie_imagen = pygame.image.load(path)
    lista.append(superficie_imagen)

    return lista


class Player:

    def __init__(self) -> None:
        
        # En la medida que vaya caminando va a ir pasando de una superficie a la otra
        self.walk = getSuperfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/hit1.png", 15, 2)

        self.stay = [] # Mientras el personaje se encuentra quieto

        self.frame = 0 # Cada fotograma que compone la imagen, para animar al personaje

        self.lives = 5 # Cant. de vidas

        self.score = 0 # Cant. puntaje

        self.animation = self.walk # El personaje comienza el juego estando quieto

        self.image = self.animation(self.frame) # Obtenemos una imagen en particular de la lista de animacion  

        self.rect = self.image.get_rect() # Dibujamos el rectangulo de nuestro personaje.


    def update(self):
        pass

    def draw(self, screen): # Dibujamos una superficie sobre otra
        screen.blit(self.image, self.rect())
