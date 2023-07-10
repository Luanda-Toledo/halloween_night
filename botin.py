import pygame
from auxiliar import Auxiliar
from constantes import *

class Coins:
    def __init__(self, x, y, w, h, type=1):
    
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
        coins_list = []  # Create an empty list to store coins
        coins_list.append(self)  # Add the current coin instance to the list
        return coins_list

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the coin image on the screen
