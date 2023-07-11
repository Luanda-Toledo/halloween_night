import pygame
from enemy import Enemy
from auxiliar import Auxiliar
from constantes import *


class EnemyEsqueletin(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, scale = 0.04)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, flip = True, scale = 0.04)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, scale = 0.04)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, flip = True, scale = 0.04)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

class EnemyZombie(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/walk/go_5.png", 0, 1, scale = 0.4)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/idle/idle_2.png", 0, 1, flip = True, scale = 0.4)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/attack/hit_2.png", 0, 1, scale = 0.4)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/attack/hit_7.png", 0, 1, flip = True, scale = 0.4)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

class EnemyFantasmin(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_der.png", 0, 1, scale = 0.05)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_der.png", 0, 1, flip = True, scale = 0.05)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_frent.png", 0, 1, scale = 0.05)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fastasmin_izqq.png", 0, 1, flip = True, scale = 0.05)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

class EnemyMurcielago(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 1, 5, scale = 0.03)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 2, 5, flip = True, scale = 0.03)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 3, 5, scale = 0.03)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 3, 5, flip = True, scale = 0.03)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

class EnemyVampiro(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_6.png", 0, 1, scale = 0.4)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_13.png", 0, 1, flip = True, scale = 0.4)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_1.png", 0, 1, scale = 0.4)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_11.png", 0, 1, flip = True, scale = 0.4)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

class EnemyEqueco(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, scale = 0.4)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, flip = True, scale = 0.4)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, scale = 0.4)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, flip = True, scale = 0.4)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump











