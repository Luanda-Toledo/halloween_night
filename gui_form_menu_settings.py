import pygame
import pygame.mixer
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from constantes import *

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # Inicializar el motor de sonido
        pygame.mixer.init()

        # Cargar el sonido de fondo
        pygame.mixer.music.load("soundtracks/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")

        # Iniciar la reproducción del sonido 
        pygame.mixer.music.play(-1)

        # BACK
        self.boton1 = Button(master = self, x = 20, y = 180, w = 180, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton1, on_click_param = "form_menu_principal", text = "BACK", font = "Times", font_size = 30, font_color = C_BLACK)

        # MUSIC
        self.boton2 = Button(master = self, x = 20, y = 20, w = 180, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/encendido.png", on_click = self.on_click_boton2, on_click_param = "form_menu_settings", text = "", font = "Times", font_size = 30, font_color = C_BLACK)

        # SOUNDS
        self.boton3 = Button(master = self, x = 20, y = 100, w = 180, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/encendido.png", on_click = self.on_click_boton3, on_click_param = "form_menu_settings", text = "", font = "Times", font_size = 30, font_color = C_BLACK)

        self.lista_widget = [self.boton1, self.boton2, self.boton3]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.boton2.image_background = "recursos/menu/apagado.png"
        else:
            pygame.mixer.music.unpause()
            self.boton2.image_background = "recursos/menu/encendido.png"
    
    def on_click_boton3(self, parametro):
        if pygame.mixer.get_busy():
            pygame.mixer.pause()
            self.boton3.image_background = "recursos/menu/apagado.png"
        else:
            pygame.mixer.unpause()
            self.boton3.image_background = "recursos/menu/encendido.png"

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()

        for aux_widget in self.lista_widget:
            aux_widget.draw()