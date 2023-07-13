import pygame
from auxiliar import Auxiliar
from constantes import *

class Coins:
    '''
    "Coins" es una clase que representa una moneda en un juego.
    '''
    def __init__(self, x, y, w, h, type=1):
        '''
        El método de inicialización de la clase recibe cinco parámetros: las coordenadas x e y para posicionar la moneda en la pantalla, el ancho y alto de la moneda, y un parámetro opcional "type" que especifica el tipo de moneda.
        Utiliza el método estático getSurfaceFromSeparateFiles de la clase "Auxiliar" para obtener una lista de superficies de imagen de monedas. Las imágenes se cargan utilizando una ruta de formato específica y se escalan y transforman según los parámetros proporcionados.
        Asigna la imagen de la moneda correspondiente al tipo especificado en el parámetro self.image.
        Crea un rectángulo que representa el área ocupada por la imagen de la moneda utilizando self.image.get_rect() y lo almacena en el atributo self.rect.
        Establece las coordenadas x e y del rectángulo utilizando self.rect.x = x y self.rect.y = y.
        Crea dos rectángulos adicionales, self.collision_rect y self.ground_collision_rect, que se utilizan para detección de colisiones con otros objetos en el juego. Ambos rectángulos se inicializan con los mismos valores que self.rect, y self.ground_collision_rect tiene una altura específica definida por la constante GROUND_COLLIDE_H.
        Crea una lista vacía self.coins_list que se utiliza para almacenar las instancias de monedas.
        '''
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("recursos/caramelos/caramel_{0}.png",1,6,flip=False,step=1,scale= 0.1,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collision_rect = pygame.Rect(self.rect)
        self.ground_collision_rect = pygame.Rect(self.rect)
        self.ground_collision_rect.height = GROUND_COLLIDE_H
        self.coins_list = []

    def lista_coins(self):
        '''
        Crea una lista vacía llamada coins_list para almacenar las monedas.
        Agrega la instancia actual de la moneda a la lista coins_list.
        Devuelve la lista coins_list.
        '''
        coins_list = []  
        coins_list.append(self)  
        return coins_list

    def draw(self, screen):
        '''
        El método draw recibe un parámetro screen, que representa la superficie de la pantalla del juego en la que se dibujará la moneda.
        Dibuja la imagen de la moneda en la pantalla utilizando screen.blit(self.image, self.rect). Esto coloca la imagen en la posición especificada por el rectángulo self.rect en la superficie screen.
        '''
        screen.blit(self.image, self.rect)
