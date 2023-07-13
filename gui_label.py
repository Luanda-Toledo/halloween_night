import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Label(Widget):
    '''
    "Label" es una subclase de "Widget" que representa una etiqueta de texto en una interfaz gráfica.
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_BLACK,color_border=C_RED,image_background=None,text="Label",font="Arial",font_size=14,font_color=C_BLUE):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades de la etiqueta de texto:
        master: La ventana principal o el widget contenedor de la etiqueta de texto.
        x, y: Las coordenadas de la posición inicial de la etiqueta de texto.
        w, h: El ancho y alto de la etiqueta de texto.
        color_background: El color de fondo de la etiqueta de texto.
        color_border: El color del borde de la etiqueta de texto.
        image_background: La imagen de fondo de la etiqueta de texto (opcional).
        text: El texto que se muestra en la etiqueta.
        font: La fuente de texto utilizada para la etiqueta.
        font_size: El tamaño de la fuente de texto.
        font_color: El color de la fuente de texto.

        Llama al método de inicialización de la clase padre (Widget) para configurar las propiedades básicas del widget.
        Renderiza la etiqueta de texto llamando al método render().
        '''
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        
        self.render()
        
    def render(self):
        '''
        Un método que se utiliza para renderizar el contenido de la etiqueta de texto. Este método llama al método render() 
        de la clase padre para configurar las propiedades básicas del widget.
        '''
        super().render()
        

    def update(self,lista_eventos):
        '''
        Un método que actualiza el estado de la etiqueta de texto en función de la lista de eventos recibidos. 
        En este caso, el método simplemente vuelve a renderizar la etiqueta de texto llamando al método render().
        '''
        self.render()

    

