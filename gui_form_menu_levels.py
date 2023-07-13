import pygame
import pygame.mixer
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button


class FormMenuLevels(Form):
    '''
    "FormMenuLevels" es una subclase de "Form" y representa un formulario para el menú de selección de niveles.
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

        Llama al método de inicialización de la clase padre "Form" utilizando super().__init__() para establecer las propiedades básicas del formulario.
        Carga y muestra las imágenes de fondo para el menú principal y los botones.
        Inicializa los botones correspondientes a cada nivel y el botón de regreso.
        Crea una lista llamada lista_widget que contiene todos los botones.
        '''
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # Imagen del fondo del menu principal
        screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        imagen_fondo = pygame.image.load("recursos/menu/menu_fondo_dos.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("HALLOWEEN NIGTH")
        screen.blit(imagen_fondo,imagen_fondo.get_rect())

        # Imagen fondo de los botones
        imagen_fondo_botones = pygame.image.load("recursos/menu/fondo_menu_uno.png")
        imagen_fondo_botones = pygame.transform.scale(imagen_fondo_botones, tamaño_img_botones)
        imagen_fondo_botones_rect = imagen_fondo_botones.get_rect()
        imagen_fondo_botones_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)
        screen.blit(imagen_fondo_botones, imagen_fondo_botones_rect)

        # LEVEL 1
        self.boton1 = Button(master = self, x = 100, y = 0, w = 180, h = 60, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton2, on_click_param = "form_game_L1", text = "LEVEL 1", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 2
        self.boton2 = Button(master = self, x = 80, y = 60, w = 220, h = 60, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton2, on_click_param = "form_game_L2", text = "LEVEL 2", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 3
        self.boton3 = Button(master = self, x = 80, y = 120, w = 220, h = 60, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton2, on_click_param = "form_game_L3", text = "LEVEL 3", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 4
        self.boton4 = Button(master = self, x = 110, y = 180, w = 160, h = 60, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton2, on_click_param = "form_game_L4", text = "LEVEL 4", font = "Times", font_size = 30, font_color = C_BLACK)

        # BACK
        self.boton5 = Button(master = self, x = 100, y = 240, w = 180, h = 60, color_background = None, color_border = None, image_background = "recursos/menu/button_two.png", on_click = self.on_click_boton1, on_click_param = "form_menu_principal", text = "BACK", font = "Times", font_size = 30, font_color = C_BLACK)


        #Lista de botones que van a aparecer en nuestro menu principal
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.boton4, self.boton5]

    def on_click_boton1(self, parametro):
        '''
        Maneja el evento de clic del botón boton5 (BACK). Cambia al formulario "form_menu_principal" 
        estableciéndolo como formulario activo.
        '''
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        '''
        Maneja el evento de clic de los botones de nivel (boton1, boton2, boton3, boton4). 
        Cambia al formulario correspondiente al nivel seleccionado estableciéndolo como formulario activo 
        y detiene la reproducción de música de fondo.
        '''
        self.set_active(parametro)
        pygame.mixer.music.stop()

    def update(self, lista_eventos,keys,delta_ms):
        '''
        Actualiza el estado del formulario y sus elementos en función de los eventos recibidos, 
        las teclas presionadas y el tiempo transcurrido desde la última actualización. 
        Actualiza los botones en la lista lista_widget.
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