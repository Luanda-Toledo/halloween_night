import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Button

class Form():
    '''
    "Form" es una clase base que representa un formulario en una interfaz gráfica.
    '''
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades del formulario:
        name: El nombre del formulario.
        master_surface: La superficie principal del formulario.
        x, y: Las coordenadas de la posición inicial del formulario.
        w, h: El ancho y alto del formulario.
        color_background: El color de fondo del formulario.
        color_border: El color del borde del formulario.
        active: Indica si el formulario está activo o no.

        Agrega el formulario actual al diccionario de formularios estático forms_dict, con el nombre del formulario como clave y el objeto formulario como valor.
        Asigna los valores de los parámetros a los atributos correspondientes del formulario.
        Crea una superficie del tamaño especificado para el formulario.
        Establece la posición de la superficie secundaria (slave_rect) dentro de la superficie principal (master_surface).
        Establece el estado activo del formulario según el valor del parámetro active.
        Si se proporciona un color de fondo, rellena la superficie con ese color.
            '''
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        if(self.color_background != None):
            self.surface.fill(self.color_background)
            
    @staticmethod
    def set_active(name):
        '''
        Un método estático que establece el formulario activo según su nombre. Itera sobre todos 
        los formularios en el diccionario forms_dict y desactiva todos los formularios, excepto el 
        formulario con el nombre especificado.
        '''
        for aux_form in Form.forms_dict.values():
            aux_form.active = False
        Form.forms_dict[name].active = True
    
    @staticmethod
    def get_active():
        '''
        Un método estático que devuelve el formulario activo actual. Itera sobre todos los 
        formularios en el diccionario forms_dict y devuelve el formulario que está activo.
        '''
        for aux_form in Form.forms_dict.values():
            if(aux_form.active):
                return aux_form
        return None

    def draw(self):
        '''
        Un método que dibuja el contenido del formulario en la superficie principal. Utiliza el método blit()
        para copiar la superficie secundaria (surface) en la superficie principal (master_surface).
        '''
        self.master_surface.blit(self.surface,self.slave_rect)
