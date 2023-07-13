import pygame
from pygame.locals import *
from constantes import *

class Widget:
    '''
    Widget representa un componente gráfico genérico en una interfaz de usuario. 
    '''
    def __init__(self,master_form,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color):
        '''
        Constructor de la clase. Recibe una serie de parámetros para inicializar las propiedades del widget, 
        como su posición, tamaño, colores, imagen de fondo, texto y estilo de fuente.
        '''
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        if image_background != None:
            self.image_background = pygame.image.load(image_background)
            self.image_background = pygame.transform.scale(self.image_background,(w, h)).convert_alpha()
        else:
            self.image_background = None
        self._text = text
        if(self._text != None):
            pygame.font.init()
            self._font_sys = pygame.font.SysFont(font,font_size)
            self._font_color = font_color

    def render(self):
        '''
        Método para renderizar el widget en la superficie maestra. Crea una superficie esclava con el tamaño 
        especificado y un rectángulo que representa la posición del widget. Luego, dibuja el fondo del widget, 
        la imagen de fondo (si se proporciona), el texto (si se proporciona) y el borde (si se especifica un 
        color de borde).
        Las propiedades principales del widget son:
        master_form: Referencia al formulario maestro al que pertenece el widget.
        x, y: Coordenadas de la posición del widget.
        w, h: Ancho y alto del widget.
        color_background: Color de fondo del widget.
        color_border: Color del borde del widget.
        image_background: Imagen de fondo del widget.
        _text: Texto del widget.
        _font_sys: Fuente del texto del widget.
        _font_color: Color del texto del widget.
        '''
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_background:
            self.slave_surface.blit(self.image_background, (0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.color_background)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self):
        pass

    def draw(self):
        '''
        Método para dibujar el widget en la superficie maestra. Utiliza el método blit de 
        la superficie maestra para dibujar la superficie esclava en la posición especificada 
        por el rectángulo del widget.
        '''
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)