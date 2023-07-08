import pygame
import math
import pygame.mixer
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_graph import Graph
from gui_label import Label
from constantes import *

class FormMenuC(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        # Inicializar el motor de sonido
        pygame.mixer.init()

        # Cargar el sonido de fondo
        pygame.mixer.music.load("soundtracks/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")

        # Iniciar la reproducción del sonido en bucle
        pygame.mixer.music.play(-1)

        self.boton1 = Button(master=self, x=0, y=150, w=200, h=40, color_background=C_GREEEN_2, color_border=C_YELLOW_2,
                             on_click=self.on_click_boton1, on_click_param="form_menu_principal", text="BACK",
                             font="Verdana", font_size=30, font_color=C_BLACK)

        self.lista_widget = [self.boton1]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.stop()

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:
            aux_widget.draw()
        
