from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    '''
    La clase "Enemy" representa a un enemigo.
    '''
    
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        '''
         El método de inicialización de la clase recibe varios parámetros que definen las propiedades del enemigo:
        x, y: Las coordenadas iniciales del enemigo en la pantalla.
        speed_walk, speed_run: Las velocidades de movimiento del enemigo al caminar y correr.
        gravity: La gravedad que afecta al enemigo.
        jump_power: La potencia del salto del enemigo.
        frame_rate_ms: El tiempo en milisegundos entre cada fotograma de animación.
        move_rate_ms: El tiempo en milisegundos entre cada movimiento del enemigo.
        jump_height: La altura máxima del salto del enemigo.
        p_scale: La escala de tamaño del enemigo (opcional, por defecto es 1).
        interval_time_jump: El intervalo de tiempo en milisegundos entre cada salto del enemigo.

        Carga las imágenes de animación para caminar y estar quieto en las direcciones derecha e izquierda utilizando el método estático getSurfaceFromSeparateFiles de la clase "Auxiliar". Las imágenes se cargan desde archivos y se escalan según los parámetros proporcionados.
        Inicializa varios atributos del enemigo.
        '''
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/nada.png", 0, 1, scale = 1)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/nada.png", 0, 1, flip = True, scale = 1)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/nada.png", 0, 1, scale = 1)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/nada.png", 0, 1, flip = True, scale = 1)

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
   
    def change_x(self,delta_x):
        '''
        Cambia la posición en el eje X del enemigo y sus rectángulos de colisión.
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        '''
        Cambia la posición en el eje Y del enemigo y sus rectángulos de colisión.
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        '''
        Realiza el movimiento del enemigo. El método actualiza el tiempo transcurrido para 
        el movimiento y verifica si el enemigo está en una plataforma o en el aire. 
        En función de eso, cambia la posición del enemigo y su animación.
        '''
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
    
    def is_on_plataform(self, plataform_list):
        '''
        Verifica si el enemigo está en una plataforma. Comprueba si el rectángulo de colisión 
        del enemigo está colisionando con algún rectángulo de colisión de una plataforma en la 
        lista de plataformas proporcionada.
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
        Realiza la animación del enemigo. El método actualiza el tiempo transcurrido 
        para la animación y cambia el fotograma actual de la animación.
        '''
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def receive_shoot(self):
        '''
        Reduce en 1 la cantidad de vidas del enemigo cuando recibe un disparo.
        '''
        self.lives -= 1

    def update(self,delta_ms,plataform_list):
        '''
        Actualiza el enemigo. Llama a los métodos do_movement y do_animation 
        para realizar el movimiento y la animación del enemigo.
        '''
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 

    def draw(self,screen):
        '''
        Dibuja el enemigo en la pantalla. Si la variable DEBUG es verdadera, 
        también dibuja los rectángulos de colisión del enemigo y su rectángulo de colisión en el suelo.
        '''
        
        if(DEBUG):
            pygame.draw.rect(screen,color=C_BLUE,rect=self.collition_rect)
            pygame.draw.rect(screen,color=C_RED,rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
