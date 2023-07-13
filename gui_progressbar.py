import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class ProgressBar(Widget):
    '''
    "ProgressBar" es una subclase de "Widget" que representa una barra de progreso en una interfaz gráfica
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None,image_progress=None,value=1,value_max=5):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades de la barra de progreso:
        master: La ventana principal o el widget contenedor de la barra de progreso.
        x, y: Las coordenadas de la posición inicial de la barra de progreso.
        w, h: El ancho y alto de la barra de progreso.
        color_background: El color de fondo de la barra de progreso.
        color_border: El color del borde de la barra de progreso.
        image_background: La imagen de fondo de la barra de progreso (opcional).
        image_progress: La imagen que representa el progreso de la barra.
        value: El valor actual de la barra de progreso.
        value_max: El valor máximo de la barra de progreso.

        Llama al método de inicialización de la clase padre (Widget) para configurar las propiedades básicas del widget.
        Carga la imagen de progreso de la barra de progreso y la escala al tamaño deseado.
        Inicializa los valores de value y value_max para determinar el progreso de la barra.
        Renderiza la barra de progreso llamando al método render().
        '''
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,None,None,None,None)
       
              
        self.surface_element = pygame.image.load(image_progress)
        self.surface_element = pygame.transform.scale(self.surface_element,(w/value_max, h)).convert_alpha()

        self.value=value
        self.value_max=value_max
        self.render()
        
    def render(self):
        '''
        Un método que se utiliza para renderizar el contenido de la barra de progreso. Este método llama 
        al método render() de la clase padre para configurar las propiedades básicas del widget y 
        luego dibuja las imágenes de progreso en función del valor actual y el valor máximo de la barra.
        '''
        super().render()
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, 0))

    def update(self,lista_eventos):
        '''
        Un método que actualiza el estado de la barra de progreso en función de la lista de eventos recibidos. En este caso, 
        el método simplemente vuelve a renderizar la barra de progreso llamando al método render().
        '''
        self.render()

    

