import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    '''
    Player representa al personaje jugador en el juego.
    '''
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        Inicializa al jugador con la posición, velocidad, gravedad, potencia de salto y otros atributos especificados.
        x (int): Posición horizontal inicial del jugador.
        y (int): Posición vertical inicial del jugador.
        speed_walk (int): Velocidad de movimiento al caminar.
        speed_run (int): Velocidad de movimiento al correr.
        gravity (int): Gravedad aplicada al jugador.
        jump_power (int): Potencia de salto del jugador.
        frame_rate_ms (int): Intervalo de tiempo entre cada fotograma de animación.
        move_rate_ms (int): Intervalo de tiempo entre cada movimiento del jugador.
        jump_height (int): Altura máxima alcanzada en un salto.
        p_scale (int): Escala del personaje (opcional). Por defecto es 1.
        interval_time_jump (int): Intervalo de tiempo mínimo entre saltos (opcional). Por defecto es 100.
        '''
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/static.png", 1, 1, flip = False, scale = 1.3)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/static.png", 1, 1, flip = True, scale = 1.3)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/jump2.png", 1, 1, flip = False, scale = 1.3)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/jump2.png", 1, 1, flip = True, scale = 1.3)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/walk1.png", 1, 1, flip = False, scale = 1.3)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/walk2.png", 1, 1, flip = True, scale = 1.3)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/hit1.png", 1, 1, flip = False, scale = 1.3, repeat_frame = 2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/hit2.png", 1, 1, flip = True, scale = 1.3, repeat_frame = 2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/kick1.png", 1, 1, flip = False, scale = 1.3,repeat_frame = 1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/personaje/sorlo/kick2.png", 1, 7, flip = True, scale = 1.3,repeat_frame = 1)

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

    def walk(self,direction):
        '''
        Hace que el jugador camine en la dirección especificada.
        direction (int): Dirección del movimiento. Puede ser DIRECTION_L (izquierda) o DIRECTION_R (derecha).
        '''
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self,on_off = True):
        '''
        Hace que el jugador dispare.
        on_off (bool): Indica si se activa o desactiva el disparo. Por defecto es True (activado).
        '''
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        '''
        Reduce una vida al jugador cuando es impactado por un disparo enemigo.
        '''
        self.lives -= 1

    def knife(self,on_off = True):
        '''
        Hace que el jugador ataque con un cuchillo.
        on_off (bool): Indica si se activa o desactiva el ataque con cuchillo. Por defecto es True (activado).
        '''
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,on_off = True):
        '''
        Hace que el jugador salte.
        on_off (bool): Indica si se activa o desactiva el salto. Por defecto es True (activado).
        '''
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            self.move_x = int(self.move_x / 2)
            self.move_y = -self.jump_power
            self.move_y = -self.jump_power
            self.frame = 0
            self.is_jump = True
            if(self.direction == DIRECTION_R):
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        '''
        Hace que el jugador se quede quieto.
        '''
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        '''
        Cambia la posición horizontal del jugador por una cantidad especificada.
        delta_x (int): Cambio en la posición horizontal.
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        '''
        Cambia la posición vertical del jugador por una cantidad especificada.
        delta_y (int): Cambio en la posición vertical.
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        '''
        Realiza los movimientos del jugador en base al tiempo transcurrido y la detección de colisiones con plataformas.
        delta_ms (int): Tiempo transcurrido desde la última actualización en milisegundos.
        plataform_list (list): Lista de plataformas con las que se detectarán colisiones.
        '''
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        '''
        Verifica si el jugador se encuentra sobre una plataforma.
        Parámetros: plataform_list (list): Lista de plataformas a verificar.
        Retorna: bool: True si el jugador se encuentra sobre una plataforma, False de lo contrario.
        '''
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self,delta_ms):
        '''
        Realiza la animación del jugador en base al tiempo transcurrido.
        delta_ms (int): Tiempo transcurrido desde la última actualización en milisegundos.
        '''
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def points(self,coin_list):
        '''
        Verifica si el jugador colisiona con una moneda y aumenta su puntaje en consecuencia.
        coin_list (list): Lista de monedas con las que se detectará la colisión.
        '''
        for coins in coin_list:
            
            if coins.rect.colliderect(self.rect):
                # If the coin collides with ALGO, remove the rectangle from the coins list
                coin_list.remove(coins)
                self.score += 1  # Increment the score by 1           
 
    def update(self,delta_ms,plataform_list,list_coin):
        '''
        Actualiza el estado del jugador en base al tiempo transcurrido, las plataformas y las monedas.
        delta_ms (int): Tiempo transcurrido desde la última actualización en milisegundos.
        plataform_list (list): Lista de plataformas.
        list_coin (list): Lista de monedas.
        '''
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.points(list_coin)
        
    
    def draw(self,screen):
        '''
        Dibuja al jugador en la pantalla.
        screen (pygame.Surface): Superficie de la pantalla donde se dibuja al jugador.
        '''
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        '''
        Procesa los eventos de entrada del jugador y actualiza su estado en consecuencia.
        delta_ms (int): Tiempo transcurrido desde la última actualización en milisegundos.
        keys (dict): Diccionario que representa el estado de las teclas presionadas.
        '''
        self.tiempo_transcurrido += delta_ms

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]and not keys[pygame.K_a] and not keys[pygame.K_s]):
            #nada presionado
            self.stay()  
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_a] and not keys[pygame.K_s] ):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_a] and not keys[pygame.K_s] ):
            self.walk(DIRECTION_R)
        
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]and not self.is_fall):
            if keys[pygame.K_RIGHT]:
                self.direction = DIRECTION_R
                self.move_x = self.speed_walk
                self.animation = self.jump_r
            elif keys[pygame.K_LEFT]:
                self.direction = DIRECTION_L
                self.move_x = -self.speed_walk
                self.animation = self.jump_l
            else:
                self.move_x = 0
            if((self.tiempo_transcurrido - self.tiempo_last_jump)> self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_s]):
            self.shoot(False)  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.move_x= 0
            self.shoot()   
        
        if(keys[pygame.K_a] and not keys[pygame.K_s]and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.move_x= 0
            self.knife()   
