import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    '''
    Plataform representa una plataforma
    '''
    def __init__(self, x, y, width, height, type = 1):
        '''
        Inicializa una plataforma con la posición, ancho y alto especificados.
        x (int): Posición horizontal de la plataforma.
        y (int): Posición vertical de la plataforma.
        width (int): Ancho de la plataforma.
        height (int): Alto de la plataforma.
        type (int): Tipo de plataforma (opcional). Por defecto es 1.
        '''
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("recursos/objetos_pantalla/plataforma/png-transparent-line-cloud-computing-white-and-gray-clouds-creative-blue-white-rectangle-thumbnail.png",
                                                                1, 18, flip = False, w = width, h = height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self, screen):
        '''
        Dibuja la plataforma en la pantalla.
        screen (pygame.Surface): Superficie de la pantalla donde se dibujará la plataforma.
        '''
        screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen, color = C_RED, rect = self.collition_rect)
            pygame.draw.rect(screen, color = C_YELLOW_2, rect = self.ground_collition_rect)
        
        