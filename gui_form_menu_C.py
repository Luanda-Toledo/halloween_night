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

        pass
        
