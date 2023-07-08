import pygame
import pygame.mixer
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        #Imagen de inicio del juego de 5 segundos 
        ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("HALLOWEEN NIGTH")

        imagen = pygame.image.load("recursos/menu/presentacion_juego.png")
        imagen = pygame.transform.scale(imagen, (800, 800))
        imagen_rect = imagen.get_rect()
        imagen_rect.center = (ventana.get_width() // 2, ventana.get_height() // 2)

        fuente = pygame.font.Font(None, 50)
        texto = fuente.render("C a r g a n d o . . .", True, (255, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = (400, 720)


        tiempo_inicial = pygame.time.get_ticks()

        while pygame.time.get_ticks() - tiempo_inicial < 5000:
            ventana.fill((0, 0, 0))
            ventana.blit(imagen, imagen_rect)
            ventana.blit(texto, texto_rect)
            pygame.display.flip()

        # Inicializar el motor de sonido
        pygame.mixer.init()

        # Cargar el sonido de fondo
        pygame.mixer.music.load("soundtracks/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")

        # Iniciar la reproducción del sonido en bucle
        pygame.mixer.music.play(-1)

        # Imagen del fondo del menu principal
        screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        imagen_fondo = pygame.image.load("recursos/menu/menu_fondo_dos.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("HALLOWEEN NIGTH")
        screen.blit(imagen_fondo,imagen_fondo.get_rect())

        # Imagen fondo de los botones
        imagen_fondo_botones = pygame.image.load("recursos/menu/fondo_menu_uno.png")
        imagen_fondo_botones = pygame.transform.scale(imagen_fondo_botones, (420, 420))
        imagen_fondo_botones_rect = imagen_fondo_botones.get_rect()
        imagen_fondo_botones_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)
        screen.blit(imagen_fondo_botones, imagen_fondo_botones_rect)

        # self.boton1 = Button(master=self,x=20,y=20,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="",text="SUMA +",font="Verdana",font_size=30,font_color=C_WHITE)
        # self.boton2 = Button(master=self,x=20,y=80,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton2,on_click_param="",text="RESTA -",font="Verdana",font_size=30,font_color=C_WHITE)
        # START
        self.boton1 = Button(master = self, x = 100, y = 20, w = 180, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_game_L4", text = "START", font = "Times", font_size = 30, font_color = C_BLACK)
        # SCORES
        self.boton2 = Button(master = self, x = 80, y = 80, w = 220, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_menu_C", text = "SCORES", font = "Times", font_size = 30, font_color = C_BLACK)
        # SETTING
        self.boton3 = Button(master = self, x = 80, y = 140, w = 220, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_menu_settings", text = "SETTING", font = "Times", font_size = 30, font_color = C_BLACK)
        # EXIT
        self.boton4 = Button(master = self, x = 110, y = 200, w = 160, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "", text = "EXIT", font = "Times", font_size = 30, font_color = C_BLACK)
        # self.boton5 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_C",text="Vector",font="Verdana",font_size=30,font_color=C_WHITE)
                                
        # self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        # self.pb1 = ProgressBar(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        # self.lista_widget = [,self.boton3,self.boton4,self.boton5,self.txt1,self.pb1]

        #Lista de botones que van a aparecer en nuestro menu principal
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.boton4]

    #def on_click_boton1(self, parametro):
        #self.pb1.value += 1
 
    #def on_click_boton2(self, parametro):
        #self.pb1.value -= 1
    
    def on_click_boton2(self, parametro):
        self.set_active(parametro)

        pygame.mixer.music.stop()

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()

        for aux_widget in self.lista_widget:    
            aux_widget.draw()