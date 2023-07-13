import pygame
import pygame.mixer
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from constantes import *

class FormMenuB(Form):
    '''
    "FormMenuB" es una subclase de "Form" y representa el formulario de ajustes
    '''
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

        Inicializa los botones correspondientes a cada opción de ajustes: BACK, MUSIC y SOUNDS.
        Crea una lista llamada lista_widget que contiene todos los botones.
        '''
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # BACK
        self.boton1 = Button(master = self, x = 100, y = 180, w = 200, h = 100, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton1, on_click_param = "form_menu_principal", text = "BACK", font = "Times", font_size = 30, font_color = C_BLACK)

        # MUSIC
        self.boton2 = Button(master = self, x = 70, y = 20, w = 280, h = 100, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton2, on_click_param = "form_menu_settings", text = " MUSIC   ON ", font = "Times", font_size = 30, font_color = C_BLACK)

        # SOUNDS
        self.boton3 = Button(master = self, x = 70, y = 100, w = 280, h = 100, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton3, on_click_param = "form_menu_settings", text = " SOUNDS   ON ", font = "Times", font_size = 30, font_color = C_BLACK)

        self.lista_widget = [self.boton1, self.boton2, self.boton3]


    def on_click_boton1(self, parametro):
        '''
        Maneja el evento de clic del botón BACK. Cambia al formulario principal estableciéndolo como formulario activo.
        '''
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        '''
        Maneja el evento de clic del botón MUSIC. Controla la reproducción y pausa de la música de fondo del juego. 
        Si la música está en reproducción, la detiene y cambia el texto del botón a "MUSIC OFF". 
        Si la música está detenida, la reproduce y cambia el texto del botón a "MUSIC ON".
        '''
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.boton2._text = " MUSIC   OFF "
        else:
            pygame.mixer.music.load("soundtracks/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")
            pygame.mixer.music.play(-1)
            self.boton2._text = " MUSIC   ON "
            
    
    def on_click_boton3(self, parametro):
        '''
        Maneja el evento de clic del botón SOUNDS. Controla la reproducción y pausa de los sonidos del juego. 
        Si los sonidos están en reproducción, los detiene y cambia el texto del botón a "SOUNDS OFF". 
        Si los sonidos están detenidos, los reproduce y cambia el texto del botón a "SOUNDS ON".
        '''
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.boton3._text = " SOUNDS   OFF "
        else:
            pygame.mixer.music.load("soundtracks/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")
            pygame.mixer.music.play(-1)
            self.boton3._text = " SOUNDS   ON "
            

    def update(self, lista_eventos, keys, delta_ms):
        '''
        Actualiza el estado del formulario y sus elementos en función de los eventos recibidos, las teclas presionadas y 
        el tiempo transcurrido desde la última actualización. Actualiza los botones en la lista lista_widget.
        '''
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        '''
        Dibuja el contenido del formulario en la superficie principal. Llama al método draw() 
        de la clase padre "Form" para dibujar el fondo y el borde. Dibuja los botones en la lista lista_widget.
        '''
        super().draw()

        for aux_widget in self.lista_widget:
            aux_widget.draw()