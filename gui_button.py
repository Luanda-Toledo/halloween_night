import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Button(Widget):
    '''
    La clase "Button" hereda de la clase "Widget" y representa un botón interactivo en una interfaz gráfica.
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None,text="Button",font="Arial",font_size=14,font_color=C_BLUE,on_click=None,on_click_param=None):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades del botón:
        master: El widget padre al que pertenece el botón.
        x, y: Las coordenadas de la posición inicial del botón.
        w, h: El ancho y alto del botón.
        color_background: El color de fondo del botón (opcional, por defecto es verde).
        color_border: El color del borde del botón (opcional, por defecto es rojo).
        image_background: La imagen de fondo del botón (opcional, por defecto es None).
        text: El texto que se muestra en el botón (opcional, por defecto es "Button").
        font: El tipo de fuente del texto (opcional, por defecto es "Arial").
        font_size: El tamaño de la fuente del texto (opcional, por defecto es 14).
        font_color: El color del texto (opcional, por defecto es azul).
        on_click: La función que se ejecuta cuando se hace clic en el botón (opcional, por defecto es None).
        on_click_param: El parámetro adicional que se pasa a la función on_click cuando se hace clic en el botón (opcional, por defecto es None).
        
        El método realiza las siguientes acciones:
        Llama al método de inicialización de la clase padre "Widget" utilizando super().__init__() para establecer las propiedades básicas del widget.
        Inicializa los atributos adicionales del botón, como on_click, on_click_param y state.
        Llama al método render() para renderizar el botón.
        '''
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)

        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.render()
        
    def render(self):
        '''
        Renderiza el botón. Llama al método render() de la clase padre "Widget" y 
        realiza modificaciones adicionales según el estado del botón. Si el estado es "M_STATE_HOVER", 
        aclara la imagen de fondo del botón, y si el estado es "M_STATE_CLICK", oscurece la imagen de fondo.
        '''
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        '''
        Actualiza el botón en función de los eventos recibidos. Verifica la posición del mouse y 
        determina el estado actual del botón (normal, hover o click). Si se produce un evento de 
        clic del mouse y el botón se encuentra en estado hover o click, ejecuta la función on_click 
        con el parámetro on_click_param. Luego, llama al método render() para actualizar la apariencia del botón.
        '''
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()

    

