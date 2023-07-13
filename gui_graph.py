import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *

class Graph(Widget):
    '''
    "Graph" es una subclase de "Widget" que representa un gráfico en una interfaz gráfica.
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades del gráfico:
        master: La ventana principal o el widget contenedor del gráfico.
        x, y: Las coordenadas de la posición inicial del gráfico.
        w, h: El ancho y alto del gráfico.
        color_background: El color de fondo del gráfico.
        color_border: El color del borde del gráfico.
        image_background: La imagen de fondo del gráfico (opcional).
    
        Llama al método de inicialización de la clase padre (Widget) para configurar las propiedades básicas del widget.
        Crea un rectángulo (surface_element) que representa el área del gráfico dentro del widget.
        Inicializa las coordenadas (x0, y0, x1, y1) para dibujar una línea en el gráfico.
        Renderiza el gráfico llamando al método render().
        '''
        super().__init__(master,x,y,w,h,color_background,color_border,None,None,None,None,None)
       
        self.surface_element = pygame.Rect(x,y,w,h)
        self.x0 = 0
        self.x1 = 100
        self.y0 = 0
        self.y1 = 100

        self.render()
        
    def render(self):
        '''
        Un método que se utiliza para renderizar el contenido del gráfico. Este método llama al método render() de la clase padre para configurar las propiedades básicas del widget y 
        luego dibuja una línea en el área del gráfico utilizando el método pygame.draw.line().
        '''
        super().render()
        pygame.draw.line(self.slave_surface,C_GREEN, (self.x0, self.y0), (self.x1, self.y1),2)

    def update(self,lista_eventos):
        '''
        Un método que actualiza el estado del gráfico en función de la lista de eventos recibidos. 
        En este caso, el método simplemente vuelve a renderizar el gráfico llamando al método render().
        '''
        self.render()

    

