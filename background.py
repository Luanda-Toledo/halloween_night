import pygame
from constantes import *


class Background:
    '''
    "Background" es una clase que representa un fondo de pantalla en un juego .
    '''

    def __init__(self, x, y,width, height,  path):
        '''
        El método de inicialización de la clase recibe cinco parámetros: las coordenadas x e y para posicionar el fondo en la pantalla, el ancho y alto del fondo, y la ruta de la imagen del fondo.

        Carga la imagen del fondo utilizando pygame.image.load(path).convert() y la almacena en el atributo self.image.
        Escala la imagen del fondo utilizando pygame.transform.scale(self.image, (width, height)) y actualiza 
        el atributo self.image con la imagen escalada.
        Crea un rectángulo que representa el área ocupada por la imagen del fondo utilizando self.image.get_rect()
        y lo almacena en el atributo self.rect.
        Establece las coordenadas x e y del rectángulo utilizando self.rect.x = x y self.rect.y = y.
        '''
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self,screen):
        screen.blit(self.image,self.rect)
       
        