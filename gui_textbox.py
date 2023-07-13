import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class TextBox(Widget):
    '''
    La clase "TextBox" hereda de la clase "Widget" y representa un campo de texto interactivo en una interfaz gráfica.
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None,text="Button",font="Arial",font_size=14,font_color=C_BLUE,on_click=None,on_click_param=None):
        '''
        El constructor __init__ recibe varios parámetros para configurar las propiedades del campo de texto, 
        como su posición, tamaño, color de fondo, borde, imagen de fondo, texto, fuente, tamaño de fuente y color de fuente. 
        Además, se puede especificar una función on_click y un parámetro on_click_param que se ejecutarán cuando 
        se haga clic en el campo de texto.
        '''
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        self.render()
        
    def render(self):
        '''
        El método render se encarga de renderizar el campo de texto en la interfaz gráfica. 
        Dependiendo del estado del campo de texto (normal, hover o click), se ajusta el brillo de la imagen de fondo.
        '''
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        '''
        El método update actualiza el estado del campo de texto en función de la lista de eventos recibidos. 
        Se verifica la posición del cursor del mouse para determinar si el campo de texto está en estado normal, 
        hover o click. Además, se manejan eventos de clic del mouse y eventos de teclado. Si se hace clic en el 
        campo de texto, se establece la bandera writing_flag en verdadero, lo que indica que se puede ingresar texto. 
        Si se presionan teclas mientras writing_flag es verdadero, se actualiza el texto del campo de texto. 
        Si se presiona la tecla "Enter", se establece writing_flag en falso, lo que indica que se ha terminado de escribir. 
        Si se presiona la tecla "Backspace", se elimina el último carácter del texto.
        '''
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(self.writing_flag):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN :
                self.writing_flag = self.slave_rect_collide.collidepoint(evento.pos)
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_RETURN:
                    self.writing_flag = False
                elif evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += evento.unicode

        self.render()

    

