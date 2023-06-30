import pygame
from doctest import FAIL_FAST
from constantes import *
from auxiliar import Auxiliar


class Player:

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height) -> None:

        # En la medida que vaya caminando va a ir pasando de una superficie a la otra
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/walk1.png", 15, 1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/walk2.png", 15, 1, True)

        # Mientras el personaje se encuentra quieto
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/static.png", 16, 1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/static.png", 16, 1, True)

        # Mientras salta
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/jump1.png", 33, 1, False, 2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("halloween_nigth/recursos/personaje/sorlo/jump1.png", 33, 1, True, 2)

        # Cada fotograma que compone la imagen, para animar al personaje
        self.frame = 0
        self.lives = 5 # Vidas
        self.score = 0 # Puntajes

        # Movimientos en x e y (valor coordenadas iniciales)
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power

        # El personaje comienza el juego estando quieto
        self.animation = self.stay_r
        self.direction = DIRECTION_R

        # Obtenemos una imagen en particular de la lista de animacion  
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect() # Dibujamos el rectangulo de nuestro personaje.
        self.rect.x = x
        self.rect.y = y

        self.is_jump = False #Flag
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0 
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0 # Valor inicial del salto en y
        self.jump_height = jump_height
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H


    def walk(self, direction): # Accion Caminar
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction

            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
        

    def jump(self, on_off = True): # Accion Saltar
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y

            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l

            self.frame = 0
            self.is_jump = True

        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self): # Estatico
        if(self.animation != self.stay_r and self.animation != self.stay_l):

            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l

            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms

        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.rect.x += self.move_x
            self.rect.y += self.move_y

            if(self.rect.y < 500):
                self.rect.y += self.gravity
            elif(self.is_jump): # SACAR
                self.jump(False)
                

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms

        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0

            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
                           
    def add_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x

    def add_y(self, delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y


    def update(self, delta_ms): # Actualizar 
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        
    
    def draw(self, screen): # Dibujamos una superficie sobre otra
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self, delta_ms, keys): 

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()

        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   

        if(keys[pygame.K_SPACE]):
            self.jump(True)

