from player import *
from constantes import *
from auxiliar import Auxiliar
import math

class Bullet():
    '''
    La clase "Bullet" representa una bala en un juego.
    '''
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,speed,path,frame_rate_ms,move_rate_ms,width=5,height=5) -> None:
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades de la bala:
        owner: El objeto que dispara la bala.
        x_init, y_init: Las coordenadas iniciales de la bala en la pantalla.
        x_end, y_end: Las coordenadas finales a las que se dirige la bala.
        speed: La velocidad de la bala.
        path: La ruta de la imagen de la bala.
        frame_rate_ms: El tiempo en milisegundos entre cada fotograma de animación.
        move_rate_ms: El tiempo en milisegundos entre cada movimiento de la bala.
        width, height: El ancho y alto de la imagen de la bala (opcional, por defecto son 5x5 píxeles).

        Carga la imagen de la bala utilizando pygame.image.load(path).convert() y la almacena en el atributo self.image.
        Escala la imagen de la bala utilizando pygame.transform.scale(self.image, (width, height)) y actualiza el atributo self.image con la imagen escalada.
        Crea un rectángulo que representa el área ocupada por la imagen de la bala utilizando self.image.get_rect() y lo almacena en el atributo self.rect.
        Establece las coordenadas x e y del rectángulo utilizando self.rect.x = x_init y self.rect.y = y_init.
        Calcula el ángulo entre las coordenadas iniciales y finales utilizando la función math.atan2() y lo almacena en la variable angle.
        Calcula las velocidades de movimiento horizontal (self.move_x) y vertical (self.move_y) de la bala utilizando las funciones trigonométricas math.cos() y math.sin() y el ángulo calculado.
        Inicializa el atributo self.is_active en True para indicar que la bala está activa.
        '''
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(y_end - y_init, x_end - x_init) #Obtengo el angulo en radianes
        print('El angulo engrados es:', int(angle*180/math.pi))

        self.move_x = math.cos(angle)*speed
        self.move_y = math.sin(angle)*speed
        
        self.is_active = True 
   
    def change_x(self,delta_x):
        '''
        El método change_x recibe un parámetro delta_x que representa el cambio en la coordenada x de la bala.
        Actualiza la coordenada x de la bala sumando delta_x a la coordenada actual (self.x += delta_x).
        Actualiza la coordenada x del rectángulo de la bala utilizando self.rect.x = int(self.x).
        '''
        self.x = self.x + delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        '''
        El método change_y recibe un parámetro delta_y que representa el cambio en la coordenada y de la bala.
        Actualiza la coordenada y de la bala sumando delta_y a la coordenada actual (self.y += delta_y).
        Actualiza la coordenada y del rectángulo de la bala utilizando self.rect.y = int(self.y).
        '''
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player):
        '''
        El método do_movement realiza el movimiento de la bala.
        Recibe un parámetro delta_ms que representa el tiempo transcurrido desde la última actualización.
        Actualiza el tiempo transcurrido para el movimiento de la bala (self.tiempo_transcurrido_move += delta_ms).
        Si el tiempo transcurrido alcanza o supera el valor de self.move_rate_ms, se realiza el movimiento de la bala.
        Llama a los métodos change_x y change_y para actualizar las coordenadas x e y de la bala según las velocidades de movimiento (self.move_x y self.move_y).
        Llama al método check_impact para comprobar si la bala colisiona con plataformas, enemigos o el jugador.
        La detección de colisiones se realiza utilizando los rectángulos de colisión (self.rect) y los rectángulos de colisión terrestre (self.ground_collision_rect).
        '''
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list,enemy_list,player)

    def do_animation(self,delta_ms):
        '''
        El método do_animation realiza la animación de la bala.
        Recibe un parámetro delta_ms que representa el tiempo transcurrido desde la última actualización.
        Actualiza el tiempo transcurrido para la animación de la bala (self.tiempo_transcurrido_animation += delta_ms).
        Si el tiempo transcurrido alcanza o supera el valor de self.frame_rate_ms, se realiza la animación de la bala.
        '''
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
    
    
    def check_impact(self,plataform_list,enemy_list,player):
        '''
        El método check_impact comprueba si la bala colisiona con plataformas, enemigos o el jugador.
        Si la bala está activa y no pertenece al mismo objeto que el jugador y colisiona con el rectángulo del jugador (self.rect.colliderect(player.rect)), se realiza la acción correspondiente (por ejemplo, reducir la vida del jugador).
        Para cada enemigo en la lista de enemigos, si la bala está activa y no pertenece al mismo objeto que el enemigo y colisiona con el rectángulo del enemigo (self.rect.colliderect(aux_enemy.rect)), se realiza la acción correspondiente.
        '''
        if(self.is_active and self.owner != player and self.rect.colliderect(player.rect)):
            print("IMPACTO PLAYER")
            player.receive_shoot()
            self.is_active = False
        for aux_enemy in enemy_list:
            if(self.is_active and self.owner != aux_enemy and self.rect.colliderect(aux_enemy.rect)):
                print("IMPACTO ENEMY")
                self.is_active = False

    def update(self,delta_ms,plataform_list,enemy_list,player):
        '''
        El método update actualiza la bala en cada fotograma del juego.
        Recibe un parámetro delta_ms que representa el tiempo transcurrido desde el último fotograma.
        Llama a los métodos do_movement y do_animation para actualizar el movimiento y la animación de la bala.
        Llama al método check_impact para comprobar si la bala colisiona con plataformas, enemigos o el jugador.
        '''
        self.do_movement(delta_ms,plataform_list,enemy_list,player)
        
        self.do_animation(delta_ms) 

    def draw(self,screen):
        '''
        El método draw dibuja la bala en la pantalla del juego.
        Si la bala está activa, dibuja la imagen de la bala en la posición especificada por el rectángulo de la bala (screen.blit(self.image, self.rect)).
        Si la constante DEBUG es verdadera, dibuja un rectángulo de colisión rojo alrededor de la bala para fines de depuración.
        '''
        if(self.is_active):
            if(DEBUG):
                pygame.draw.rect(screen,color=color_bullets,rect=self.collition_rect)
            screen.blit(self.image,self.rect)
